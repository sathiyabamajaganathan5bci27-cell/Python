from itertools import groupby

# Read the input string
s = input()

# Group consecutive characters
# k is the character, g is the iterator of the group
result = []
for k, g in groupby(s):
    # Calculate the number of occurrences (length of group)
    count = len(list(g))
    # Format as (count, character)
    result.append(f"({count}, {k})")

# Print the list as a space-separated string
print(" ".join(result))
