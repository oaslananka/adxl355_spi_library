"""
File        : tests\test_adxl355.py
Description : Test cases for the ADXL355 accelerometer library.
Author      : oaslananka
GitHub      : https://github.com/oaslananka
"""

import unittest
from adxl355 import Adxl355

class TestAdxl355(unittest.TestCase):
    def setUp(self):
        """Test setup that runs before each test method."""
        self.accelerometer = Adxl355()
    
    def test_get_axis(self):
        """Test the get_axis method for expected return types."""
        x, y, z = self.accelerometer.get_axis()
        self.assertIsInstance(x, float, "X should be a float")
        self.assertIsInstance(y, float, "Y should be a float")
        self.assertIsInstance(z, float, "Z should be a float")
    
    def test_get_x(self):
        """Test if get_x returns a float."""
        x = self.accelerometer.get_x()
        self.assertIsInstance(x, float, "X should be a float")
    
    def test_get_y(self):
        """Test if get_y returns a float."""
        y = self.accelerometer.get_y()
        self.assertIsInstance(y, float, "Y should be a float")
    
    def test_get_z(self):
        """Test if get_z returns a float."""
        z = self.accelerometer.get_z()
        self.assertIsInstance(z, float, "Z should be a float")

    def test_spi_configuration(self):
        """Test if SPI configuration is correctly set."""
        self.assertEqual(self.accelerometer.spi.max_speed_hz, 10000000, "SPI max speed should be 10MHz")
        self.assertEqual(self.accelerometer.spi.mode, 0b00, "SPI mode should be 0")

    def test_drdy_pin_configuration(self):
        """Test the configuration of the DRDY pin."""
        self.assertEqual(self.accelerometer.drdy_pin, 11, "DRDY pin should be 11")
    
    def test_conversion_accuracy(self):
        """Test conversion accuracy by providing a known raw value."""
        raw_value = 0x1FFFFF  # Max positive value for 21-bit ADC
        expected_value = -1  # Because of two's complement and test method
        converted_value = self.accelerometer.convert_to_signed(raw_value)
        self.assertEqual(converted_value, expected_value, "Conversion should handle two's complement correctly")

# Run the tests
if __name__ == '__main__':
    unittest.main()
