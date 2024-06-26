
# ADXL355 SPI Library

Welcome to the ADXL355 SPI Library, a comprehensive Python library for interfacing with the ADXL355 accelerometer via SPI communication. This library is designed to provide a simple and intuitive API for accessing the full capabilities of the ADXL355 sensor, allowing for both basic and advanced accelerometer data handling.

## Features

- **Easy-to-use**: Simple functions to read and write data from the ADXL355.
- **Real-Time Data Acquisition**: Support for real-time acceleration data acquisition and processing.
- **Conversion Utilities**: Includes utilities for converting raw sensor data into meaningful units (g, cm/s²).
- **Comprehensive Examples**: Includes several examples demonstrating the library's capabilities.

## Installation

Clone this repository and install the package using pip:

```bash
git clone https://github.com/oaslananka/adxl355_spi_library.git
cd adxl355_spi_library
pip install .
```

## Usage

Import the library and initialize the accelerometer:

```python
from adxl355 import Adxl355

accelerometer = Adxl355()
```

To read acceleration data:

```python
x, y, z = accelerometer.get_axis()
print(f"Acceleration - X: {x} g, Y: {y} g, Z: {z} g")
```

For detailed examples, refer to the `examples/` directory.

## Documentation

For more detailed information about the library's API and functionalities, visit the [documentation](https://github.com/oaslananka/adxl355_spi_library#readme).

## Contributing

Contributions are welcome! Please refer to our `CONTRIBUTING.md` for guidelines on how to make contributions to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **[oaslananka](https://github.com/oaslananka)**

## Acknowledgments

- Thanks to everyone who has contributed to this project!
