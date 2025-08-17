"""
File        : improved_odr_example.py
Description : Demonstrates proper ODR (Output Data Rate) usage of the ADXL355 accelerometer library.
              This example shows how to correctly set and use different ODR values.
Author      : oaslananka
GitHub      : https://github.com/oaslananka
"""

import time
from adxl355 import Adxl355

def test_odr_rates():
    """Test different ODR rates and measure actual sampling frequency."""
    
    # Available ODR rates to test
    odr_rates = [125, 250, 500, 1000, 2000, 4000]
    
    for odr in odr_rates:
        print(f"\n=== Testing ODR: {odr} Hz ===")
        
        try:
            # Initialize accelerometer with specific ODR
            accelerometer = Adxl355()
            accelerometer.set_filter(odr, 0)  # Set ODR, no high-pass filter
            
            # Wait for settings to take effect
            time.sleep(0.1)
            
            # Measure actual sampling rate
            sample_count = 0
            start_time = time.time()
            test_duration = 1.0  # Test for 1 second
            
            print(f"Measuring actual sampling rate for {test_duration} seconds...")
            
            while (time.time() - start_time) < test_duration:
                x, y, z = accelerometer.get_axis()
                sample_count += 1
                
                # Optional: Print some samples
                if sample_count <= 5:
                    print(f"Sample {sample_count}: X: {x:.3f}g, Y: {y:.3f}g, Z: {z:.3f}g")
            
            actual_rate = sample_count / test_duration
            print(f"Expected ODR: {odr} Hz")
            print(f"Actual rate: {actual_rate:.1f} Hz")
            print(f"Difference: {abs(odr - actual_rate):.1f} Hz")
            
            # Check if the rate is within acceptable range (±10%)
            if abs(odr - actual_rate) / odr < 0.1:
                print("✅ ODR is working correctly!")
            else:
                print("❌ ODR mismatch detected!")
                
        except Exception as e:
            print(f"Error testing ODR {odr}: {e}")

def main():
    """Main function to test ODR functionality."""
    print("ADXL355 Accelerometer - ODR Testing")
    print("This script will test different Output Data Rates")
    
    try:
        test_odr_rates()
        
    except KeyboardInterrupt:
        print("\nTesting stopped by user. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
