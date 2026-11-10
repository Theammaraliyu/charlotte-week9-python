
# Charlotte Projects - Week 9 Class 1 Homework
# Python Fundamentals and Engineering Unit Conversion

# Question 9: Well information
well_id = "WELL-09"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

# Convert pressure from psi to kPa
pressure_kpa = pressure_psi * 6.8947572932

# Convert temperature from Fahrenheit to Celsius
temperature_c = (temperature_f - 32) * 5 / 9

# Display the drilling telemetry report
print("DRILLING TELEMETRY REPORT")
print("------------------------")
print(f"Well ID: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor Active: {sensor_active}")


# Question 10: Test with different measurements
pressure_psi = 3000.0
temperature_f = 32.0

pressure_kpa = pressure_psi * 6.8947572932
temperature_c = (temperature_f - 32) * 5 / 9

print("\nSECOND TEST")
print("-----------")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")


# Question 11: Demonstrating a type mismatch
raw_pressure = "3150"

# This line causes a TypeError because raw_pressure is a string.
# pressure_kpa = raw_pressure * 6.8947572932

# Convert the string value to a float
pressure_psi = float(raw_pressure)

# Calculate pressure in kPa
pressure_kpa = pressure_psi * 6.8947572932

# Display the data types and converted pressure
print("\nTYPE CONVERSION DEMONSTRATION")
print("-----------------------------")
print(f"Original data type: {type(raw_pressure)}")
print(f"Converted data type: {type(pressure_psi)}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
