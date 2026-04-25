# Read the total number of stamps
n = int(input())

# Initialize an empty set
stamps = set()

# Add each country to the set
for _ in range(n):
    stamps.add(input())

# Print the number of unique elements in the set
print(len(stamps))
