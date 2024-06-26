from setuptools import setup, find_packages

setup(
    name='adxl355_library',
    version='0.1.0',
    author='oaslananka',
    author_email='info@oaslananka.dev',
    description='A Python library for interfacing with the ADXL355 accelerometer via SPI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oaslananka/adxl355_spi_library',
    packages=find_packages(),
    install_requires=[
        'spidev',  # SPI interface for Raspberry Pi
        'wiringpi'  # GPIO access library
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='ADXL355 accelerometer SPI hardware',
    project_urls={
        'Documentation': 'https://github.com/oaslananka/adxl355_spi_library#readme',
        'Source': 'https://github.com/oaslananka/adxl355_spi_library',
        'Tracker': 'https://github.com/oaslananka/adxl355_spi_library/issues',
    },
    python_requires='>=3.6',
    zip_safe=False,
    include_package_data=True,
)