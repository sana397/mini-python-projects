# Data Logger: Store and analyze 5 predefined sensor readings
# Create a list with 5 predefined temperature readings
temp_list = [23.5, 25.1, 22.8, 26.3, 24.7]

# Print all readings with Unicode degree symbol
print("Sensor Readings:")
for temp in temp_list:
    print(f"{temp}\u00B0C")

# Calculate and print the average temperature
average = sum(temp_list) / len(temp_list) if len(temp_list) > 0 else 0
print(f"\nAverage temperature: {average:.1f}\u00B0C")