import math

def calculate_coil_dimensions(wire_length, material):
    # Constants for sacred cubit ratios
    sacred_cubit_ratio = 1.618  # Golden ratio
    base_length_ratio = sacred_cubit_ratio / (math.pi * 2)

    # Calculate the base length and height based on the wire length
    base_length = wire_length / (1 + base_length_ratio)
    height = base_length * base_length_ratio

    # Calculate angles
    angle_x = math.degrees(math.atan(height / base_length))
    angle_y = 90 - angle_x
    angle_z = 90

    # Return the results
    return base_length, height, angle_x, angle_y, angle_z

# Prompt the user for the desired length of wire in feet
wire_length_feet = float(input("Enter the desired length of wire (in feet): "))

# Prompt the user for the material selection
material = input("Enter the material (copper, steel, aluminum, quartz): ")

# Convert wire length from feet to inches
wire_length_inches = wire_length_feet * 12

# Calculate coil dimensions
base_length, height, angle_x, angle_y, angle_z = calculate_coil_dimensions(wire_length_inches, material)

# Display the results
print(f"Wire length: {wire_length_inches} inches")
print(f"Base length: {base_length} inches")
print(f"Height: {height} inches")
print(f"Angle X: {angle_x} degrees")
print(f"Angle Y: {angle_y} degrees")
print(f"Angle Z: {angle_z} degrees")
