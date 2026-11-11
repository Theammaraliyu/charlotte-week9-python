
# Week 9 Class 2 - Python Collections

measurement_units = ("psi", "degF")

# List of eight well sensor observations
readings = [
    {"well_id": "WELL-07", "pressure_psi": 3150.0, "temperature_f": 186.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-08", "pressure_psi": 2780.0, "temperature_f": 172.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-09", "pressure_psi": 3325.0, "temperature_f": 195.0, "sensor_active": False, "field": "north"},
    {"well_id": "WELL-10", "pressure_psi": 2890.0, "temperature_f": 180.0, "sensor_active": True, "field": "east"},
    {"well_id": "WELL-11", "pressure_psi": 3040.0, "temperature_f": 188.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-07", "pressure_psi": 3180.0, "temperature_f": 187.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-12", "pressure_psi": 2510.0, "temperature_f": 166.0, "sensor_active": False, "field": "east"},
    {"well_id": "WELL-08", "pressure_psi": 2815.0, "temperature_f": 174.0, "sensor_active": True, "field": "south"}
]

# Count all observations
print("Total observations:", len(readings))


# Display the first two observations
print("\nThe first two observations are:")
print(readings[0:2])

# Display the last observation
print("\nThe last observation is:")
print(readings[-1])


# Get unique well IDs
well_ids = set()

for reading in readings:
    well_ids.add(reading["well_id"])

print("\nDistinct well IDs:", sorted(well_ids))

# Get unique fields
fields = set()

for reading in readings:
    fields.add(reading["field"])

print("Distinct fields:", sorted(fields))


# Display measurement units
print("\nPressure unit:", measurement_units[0])
print("Temperature unit:", measurement_units[1])


# Get all pressure readings
pressures = []

for reading in readings:
    pressures.append(reading["pressure_psi"])

# Calculate total and average pressure
total_pressure = sum(pressures)
average_pressure = total_pressure / len(pressures)

print("\nTotal pressure:", total_pressure, "psi")
print("Average pressure:", average_pressure, "psi")


# Count observations for each well
well_counts = {}

for reading in readings:
    well_id = reading["well_id"]

    if well_id in well_counts:
        well_counts[well_id] += 1
    else:
        well_counts[well_id] = 1

print("\nNumber of observations per well:")

for well_id in sorted(well_counts):
    print(well_id, ":", well_counts[well_id])


# Count inactive sensors
inactive_count = 0

for reading in readings:
    if reading["sensor_active"] == False:
        inactive_count += 1

print("\nInactive sensor observations:", inactive_count)


# Find the second WELL-07 pressure reading
well_07_readings = []

for reading in readings:
    if reading["well_id"] == "WELL-07":
        well_07_readings.append(reading)

print("Second WELL-07 pressure:",
      well_07_readings[1]["pressure_psi"], "psi")
