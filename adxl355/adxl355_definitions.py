"""
Module      : adxl355_definitions.py
Description : Contains definitions and constants for the ADXL355 accelerometer library.
Author      : oaslananka
GitHub      : https://github.com/oaslananka
"""

# Constants for SPI configuration
SPI_MAX_CLOCK_HZ = 10_000_000  # Maximum SPI clock frequency
SPI_MODE = 0b00               # SPI communication mode
SPI_BUS = 0                   # SPI bus number
SPI_DEVICE = 0                # SPI device number

# Constants for DRDY (Data Ready) pin configuration
DRDY_PIN = 11                 # GPIO pin number for DRDY
DRDY_DELAY = 0.000001         # Delay in seconds while polling DRDY pin
DRDY_TIMEOUT = 2              # Timeout in seconds for DRDY pin

# Register addresses
REG_DEVID_AD = 0x00           # Device ID
REG_DEVID_MST = 0x01          # MEMS device ID
REG_PARTID = 0x02             # Part ID
REG_REVID = 0x03              # Revision ID
REG_STATUS = 0x04             # Status
REG_FIFO_ENTRIES = 0x05       # FIFO entries
REG_TEMP2 = 0x06              # Temperature data (MSB)
REG_TEMP1 = 0x07              # Temperature data (LSB)
REG_XDATA3 = 0x08             # X-axis data (MSB)
REG_XDATA2 = 0x09             # X-axis data (middle)
REG_XDATA1 = 0x0A             # X-axis data (LSB)
REG_YDATA3 = 0x0B             # Y-axis data (MSB)
REG_YDATA2 = 0x0C             # Y-axis data (middle)
REG_YDATA1 = 0x0D             # Y-axis data (LSB)
REG_ZDATA3 = 0x0E             # Z-axis data (MSB)
REG_ZDATA2 = 0x0F             # Z-axis data (middle)
REG_ZDATA1 = 0x10             # Z-axis data (LSB)
REG_FIFO_DATA = 0x11          # FIFO data
REG_OFFSET_X_H = 0x1E         # X-axis offset (MSB)
REG_OFFSET_X_L = 0x1F         # X-axis offset (LSB)
REG_OFFSET_Y_H = 0x20         # Y-axis offset (MSB)
REG_OFFSET_Y_L = 0x21         # Y-axis offset (LSB)
REG_OFFSET_Z_H = 0x22         # Z-axis offset (MSB)
REG_OFFSET_Z_L = 0x23         # Z-axis offset (LSB)
REG_ACT_EN = 0x24             # Activity enable
REG_ACT_THRESH_H = 0x25       # Activity threshold (MSB)
REG_ACT_THRESH_L = 0x26       # Activity threshold (LSB)
REG_ACT_COUNT = 0x27          # Activity count
REG_FILTER = 0x28             # Filter control
REG_FIFO_SAMPLES = 0x29       # FIFO samples
REG_INT_MAP = 0x2A            # Interrupt mapping
REG_SYNC = 0x2B               # Synchronization control
REG_RANGE = 0x2C              # Range control
REG_POWER_CTL = 0x2D          # Power control
REG_SELF_TEST = 0x2E          # Self-test control
REG_RESET = 0x2F              # Reset control

# Range settings
RANGE_2G = 0b01               # ±2g
RANGE_4G = 0b10               # ±4g
RANGE_8G = 0b11               # ±8g

# Output data rates (ODR)
ODR_4000 = 0b0000             # 4000-1000 Hz
ODR_2000 = 0b0001             # 2000-500 Hz
ODR_1000 = 0b0010             # 1000-250 Hz
ODR_500 = 0b0011              # 500-125 Hz
ODR_250 = 0b0100              # 250-62.5 Hz
ODR_125 = 0b0101              # 125-31.5 Hz
ODR_62_5 = 0b0110             # 62.5-15.625 Hz
ODR_31_25 = 0b0111            # 31.25-7.813 Hz
ODR_15_625 = 0b1000           # 15.625-3.906 Hz
ODR_7_813 = 0b1001            # 7.813-1.953 Hz
ODR_3_906 = 0b1010            # 3.906-0.977 Hz

# High-pass filter coefficients (HPFC)
HPFC_0 = 0b000                # Disabled
HPFC_1 = 0b001                # Filter at 24.70 x 10^-4 x ODR
HPFC_2 = 0b010                # Filter at 6.208 x 10^-4 x ODR
HPFC_3 = 0b011                # Filter at 1.554 x 10^-4 x ODR
HPFC_4 = 0b100                # Filter at 0.386 x 10^-4 x ODR
HPFC_5 = 0b101                # Filter at 0.095 x 10^-4 x ODR
HPFC_6 = 0b110                # Filter at 0.023 x 10^-4 x ODR

# Dictionary mappings
RANGE_TO_BIT = {
    2.048: RANGE_2G,
    4.096: RANGE_4G,
    8.192: RANGE_8G
}
ODR_TO_BIT = {
    4000: ODR_4000,
    2000: ODR_2000,
    1000: ODR_1000,
    500: ODR_500,
    250: ODR_250,
    125: ODR_125,
    62.5: ODR_62_5,
    31.25: ODR_31_25,
    15.625: ODR_15_625,
    7.813: ODR_7_813,
    3.906: ODR_3_906
}
HPFC_TO_BIT = {
    0: HPFC_0,
    1: HPFC_1,
    2: HPFC_2,
    3: HPFC_3,
    4: HPFC_4,
    5: HPFC_5,
    6: HPFC_6
}
