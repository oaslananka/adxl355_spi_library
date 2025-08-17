# ADXL355 ODR Configuration Fix

## Issue Analysis

The reported problem where ODR settings don't work correctly and always getting ~11,000 measurements per second has been identified and fixed.

## Root Causes

1. **Missing `start()` and `stop()` methods**: The library was calling these methods but they weren't defined, causing the accelerometer to not properly restart after configuration changes.

2. **Improper timing in examples**: The example code used fixed delays instead of respecting the configured ODR.

3. **DRDY pin polling inefficiency**: The current implementation polls the DRDY pin continuously, which can lead to timing issues.

## Fixes Applied

### 1. Added Missing Methods

```python
def start(self):
    """Starts the ADXL355 accelerometer by setting the measurement mode."""
    self.write_register(REG_POWER_CTL, 0x00)  # Measurement mode

def stop(self):
    """Stops the ADXL355 accelerometer by setting standby mode."""
    self.write_register(REG_POWER_CTL, 0x01)  # Standby mode
```

### 2. Improved ODR Tracking

Modified the `__init__` and `set_filter` methods to properly track the current ODR:

```python
# Store current ODR for timing calculations
self.current_odr = odr
```

### 3. Created Proper ODR Testing Example

A new example file (`improved_odr_example.py`) that:
- Tests different ODR rates systematically
- Measures actual sampling frequencies
- Validates ODR configuration is working correctly

## Recommendations for Your Use Case

### For Raspberry Pi 5/Zero 2 Usage:

1. **Use appropriate ODR**: For your application, start with 250-500 Hz instead of 4000 Hz to avoid overwhelming the system.

2. **Proper delay calculation**: Instead of fixed delays, use:
   ```python
   expected_interval = 1.0 / odr  # seconds between samples
   ```

3. **DRDY pin optimization**: Consider using interrupt-based reading instead of polling:
   ```python
   # Set up GPIO interrupt for DRDY pin
   wp.wiringPiISR(self.drdy_pin, wp.INT_EDGE_RISING, self.data_ready_callback)
   ```

### Example Usage:

```python
# Initialize with specific ODR
accelerometer = Adxl355()
accelerometer.set_filter(250, 0)  # 250 Hz ODR

# Read data with proper timing
while True:
    x, y, z = accelerometer.get_axis()
    print(f"X: {x:.3f}g, Y: {y:.3f}g, Z: {z:.3f}g")
    # No fixed delay needed - get_axis() handles timing
```

## Testing

Run the new test example to verify ODR is working:
```bash
python examples/improved_odr_example.py
```

This should show actual sampling rates matching the configured ODR values.

## Notes

- The wiringpi library dependency issue mentioned is a known problem on newer Raspberry Pi OS versions
- Consider migrating to GPIO libraries like RPi.GPIO or gpiozero for better compatibility
- The DRDY pin timing should now work correctly with proper start/stop sequences
