import math

# Input side lengths
ab = int(input())
bc = int(input())

# Calculate the angle in radians and convert to degrees
# Since angle MBC = angle BCA, we find atan(AB/BC)
angle_rad = math.atan2(ab, bc)
angle_deg = math.degrees(angle_rad)

# Round to nearest integer as per instructions
# Use chr(176) for the degree symbol
print(f"{round(angle_deg)}{chr(176)}")
