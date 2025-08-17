"""
Module      : adxl355_spi.py
Description : This module contains the SPI library functions for the ADXL355 accelerometer.
Author      : oaslananka
GitHub      : https://github.com/oaslananka
"""

import spidev
import time
import wiringpi as wp
from adxl355_definitions import *


class Adxl355:
    """
    A class representing the ADXL355 accelerometer.

    This class provides methods to read acceleration values from the ADXL355 accelerometer
    using SPI communication.

    Attributes:
        spi: An instance of the `spidev.SpiDev` class for SPI communication.
        drdy_pin: The GPIO pin number for the DRDY (data ready) interrupt.
        drdy_delay: The delay between DRDY pin checks.
        drdy_timeout: The maximum time to wait for the DRDY pin to go high.
        factor: The conversion factor to convert raw acceleration values to g units.

    Methods:
        read_register: Reads the value of a register.
        write_register: Writes a value to a register.
        wait_for_data_ready: Waits for the DRDY pin to go high.
        set_range: Sets the measurement range of the accelerometer.
        set_filter: Sets the output data rate and high-pass filter cutoff frequency.
        get_x_raw: Reads the raw X-axis acceleration value.
        get_y_raw: Reads the raw Y-axis acceleration value.
        get_z_raw: Reads the raw Z-axis acceleration value.
        convert_to_signed: Converts a raw value to a signed value.
        get_axis: Reads the X, Y, and Z-axis acceleration values.
        get_x: Reads the X-axis acceleration value in g units.
        get_y: Reads the Y-axis acceleration value in g units.
        get_z: Reads the Z-axis acceleration value in g units.
    """

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(SPI_BUS, SPI_DEVICE)
        self.spi.max_speed_hz = SPI_MAX_CLOCK_HZ
        self.spi.mode = SPI_MODE

        wp.wiringPiSetupPhys()
        self.drdy_pin = DRDY_PIN
        self.drdy_delay = DRDY_DELAY
        self.drdy_timeout = DRDY_TIMEOUT

        range_g = 2.048
        odr = 125
        hpfc = 0

        self.transfer = self.spi.xfer2
        self.set_range(range_g)
        self.set_filter(odr, hpfc)
        
        # Store current ODR for timing calculations
        self.current_odr = odr
        self.wait_for_data_ready()

        self.factor = (range_g * 2) / 2**20

    def read_register(self, register, length=1):
        """
        Reads the value of a register.

        Args:
            register (int): The register address.
            length (int, optional): The number of bytes to read. Defaults to 1.

        Returns:
            int or list: The value(s) read from the register.
        """
        address = (register << 1) | 0b1
        if length == 1:
            result = self.transfer([address, 0x00])
            return result[1]
        else:
            result = self.transfer([address] + [0x00] * (length))
            return result[1:]

    def write_register(self, register, value):
        """
        Writes a value to a register.

        Args:
            register (int): The register address.
            value (int): The value to write to the register.
        """
        address = (register << 1) & 0b11111110
        self.transfer([address, value])

    def wait_for_data_ready(self):
        """
        Waits for the DRDY pin to go high.
        """
        start = time.time()
        elapsed = time.time() - start
        if self.drdy_pin is not None:
            drdy_level = wp.digitalRead(self.drdy_pin)
            while (drdy_level == wp.LOW) and (elapsed < self.drdy_timeout):
                elapsed = time.time() - start
                drdy_level = wp.digitalRead(self.drdy_pin)
                time.sleep(self.drdy_delay)
            if elapsed >= self.drdy_timeout:
                print("***---Timeout occurred while polling DRDY pin---***")
        else:
            time.sleep(self.drdy_timeout)
            print("***---DRDY pin not connected---***")

    def set_range(self, range_g):
        """
        Sets the measurement range of the accelerometer.

        Args:
            range_g (float): The measurement range in g units.
        """
        self.stop()
        temp = self.read_register(REG_RANGE)
        self.write_register(REG_RANGE, (temp & 0b11111100)
                            | RANGE_TO_BIT[range_g])
        self.start()

    def set_filter(self, odr, hpfc):
        """
        Sets the output data rate and high-pass filter cutoff frequency.

        Args:
            odr (int): The output data rate in Hz.
            hpfc (int): The high-pass filter cutoff frequency in Hz.
        """
        self.stop()
        self.write_register(
            REG_FILTER, (HPFC_TO_BIT[hpfc] << 4) | ODR_TO_BIT[odr])
        self.current_odr = odr  # Store current ODR for timing
        self.start()

    def get_x_raw(self):
        """
        Reads the raw X-axis acceleration value.

        Returns:
            int: The raw X-axis acceleration value.
        """
        data = self.read_register(REG_XDATA3, 3)
        raw_value = (data[2] >> 4) | (data[1] << 4) | (data[0] << 12)
        return self.convert_to_signed(raw_value)

    def get_y_raw(self):
        """
        Reads the raw Y-axis acceleration value.

        Returns:
            int: The raw Y-axis acceleration value.
        """
        data = self.read_register(REG_YDATA3, 3)
        raw_value = (data[2] >> 4) | (data[1] << 4) | (data[0] << 12)
        return self.convert_to_signed(raw_value)

    def get_z_raw(self):
        """
        Reads the raw Z-axis acceleration value.

        Returns:
            int: The raw Z-axis acceleration value.
        """
        data = self.read_register(REG_ZDATA3, 3)
        raw_value = (data[2] >> 4) | (data[1] << 4) | (data[0] << 12)
        return self.convert_to_signed(raw_value)

    def convert_to_signed(self, value):
        """
        Converts a raw value to a signed value.

        Args:
            value (int): The raw value.

        Returns:
            int: The signed value.
        """
        if (0x80000 & value):
            return - (0x0100000 - value)
        return value

    def get_axis(self):
        """
        Reads the X, Y, and Z-axis acceleration values.

        Returns:
            tuple: A tuple containing the X, Y, and Z-axis acceleration values.
        """
        self.wait_for_data_ready()
        return self.get_x(), self.get_y(), self.get_z()

    def get_x(self):
        """
        Reads the X-axis acceleration value in g units.

        Returns:
            float: The X-axis acceleration value.
        """
        return float(self.get_x_raw()) * self.factor

    def get_y(self):
        """
        Reads the Y-axis acceleration value in g units.

        Returns:
            float: The Y-axis acceleration value.
        """
        return float(self.get_y_raw()) * self.factor

    def get_z(self):
        """
        Reads the Z-axis acceleration value in g units.

        Returns:
            float: The Z-axis acceleration value.
        """
        return float(self.get_z_raw()) * self.factor

    def start(self):
        """
        Starts the ADXL355 accelerometer by setting the measurement mode.
        """
        self.write_register(REG_POWER_CTL, 0x00)  # Measurement mode

    def stop(self):
        """
        Stops the ADXL355 accelerometer by setting standby mode.
        """
        self.write_register(REG_POWER_CTL, 0x01)  # Standby mode
