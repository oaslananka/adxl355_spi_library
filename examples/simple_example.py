"""
File        : simple_example.py
Description : Demonstrates basic usage of the ADXL355 accelerometer library by continuously
              reading and printing acceleration data from the X, Y, and Z axes.
Author      : oaslananka
GitHub      : https://github.com/oaslananka
"""

import time
from adxl355 import Adxl355

def main():
    """Main function to initialize the accelerometer and read the axis data continuously."""
    accelerometer = Adxl355()
    print("ADXL355 Accelerometer - Continuous Data Read")

    try:
        # Continuous data read loop
        while True:
            x, y, z = accelerometer.get_axis()
            print(f"Acceleration -> X: {x:.3f} g, Y: {y:.3f} g, Z: {z:.3f} g")
            time.sleep(0.1)  # Delay to reduce output frequency for readability

    except KeyboardInterrupt:
        # Graceful exit upon interrupt
        print("Measurement stopped by user. Exiting...")

if __name__ == "__main__":
    main()
