
# Charlotte Projects - Week 9 Class 1 Homework
# Python Fundamentals and Engineering Unit Conversion

# Well information
well_id = "WELL-09"
pressure_psi = 3000.0
temperature_f = 32.0
sensor_active = True

# Convert pressure from psi to kPa
pressure_kpa = pressure_psi * 6.8947572932

# Convert temperature from Fahrenheit to Celsius
temperature_c = (temperature_f - 32) * 5 / 9

# Display the results
print("DRILLING TELEMETRY REPORT")
print("------------------------")
print(f"Well ID: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor Active: {sensor_active}")

# Question 11: Demonstrating a type mismatch

raw_pressure = "3150"

# Intentional type mismatch (commented out)
# pressure_kpa = raw_pressure * 6.8947572932

# Convert string to float
pressure_psi = float(raw_pressure)

# Calculate pressure in kPa
pressure_kpa = pressure_psi * 6.8947572932

# Display the results
print("\nTYPE CONVERSION DEMONSTRATION")
print(f"Original data type: {type(raw_pressure)}")
print(f"Converted data type: {type(pressure_psi)}")
print(f"Pressure: {pressure_kpa:.1f} kPa")