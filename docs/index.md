
# ADXL355 SPI Library Documentation

Welcome to the documentation of the ADXL355 SPI Library. This library provides an interface for the ADXL355 accelerometer via SPI, allowing users to easily access and utilize the advanced features of this sensor.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

The ADXL355 is a low noise, digital output, triaxial accelerometer with a wide range of functionalities and digital features. This library is designed to simplify the process of integrating the ADXL355 with your projects, providing both basic and advanced functionalities.

## Installation

To install the ADXL355 SPI Library, you will need Python 3.6 or higher. Installation is straightforward using pip:

```bash
pip install adxl355_spi_library
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/oaslananka/adxl355_spi_library.git
cd adxl355_spi_library
pip install .
```

## Getting Started

Here are the initial steps to get started with the ADXL355 SPI Library:

1. Import the library:
   ```python
   from adxl355 import Adxl355
   ```

2. Initialize the sensor:
   ```python
   accelerometer = Adxl355()
   ```

3. Read acceleration data:
   ```python
   x, y, z = accelerometer.get_axis()
   print(f"Acceleration - X: {x} g, Y: {y} g, Z: {z} g")
   ```

## API Reference

The library includes several functions for interacting with the ADXL355 accelerometer. Key functions include:

- `get_axis()`: Returns the current acceleration readings in the X, Y, and Z axes.
- `set_range(range_g)`: Sets the measurement range of the accelerometer.
- `set_filter(odr, hpfc)`: Configures the output data rate and high-pass filter settings.

Full API documentation can be found in the source code comments.

## Examples

Check the `examples/` directory in the GitHub repository for sample scripts demonstrating how to use the library in various scenarios.

## Contributing

Contributions to the ADXL355 SPI Library are welcome. Please review the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file in the GitHub repository for more details.
