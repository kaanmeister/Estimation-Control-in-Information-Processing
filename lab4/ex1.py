import numpy as np

def calibrate_sensor(readings):
    """
    Computes the best-fit constant temperature from a list of readings.
    """
    # 1. Sensor readings
    y = np.array(readings)
    
    # 2 & 3. Compute x that best fits the data (the arithmetic mean)
    x = np.mean(y)
    
    return x
sensor_readings = [21, 22, 23, 24]

#compute calibrated temperature
calibrated_temp = calibrate_sensor(sensor_readings)
print(f"Sensor Readings (y): {sensor_readings}")
print(f"Best-fit True Temperature (x): {calibrated_temp}°C")