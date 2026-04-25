# Read n and m
n, m = map(int, input().split())

# Read the array elements
array = list(map(int, input().split()))

# Read sets A and B (convert to set for O(1) lookups)
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = 0

# Iterate through the array once
for i in array:
    if i in set_a:
        happiness += 1
    elif i in set_b:
        happiness -= 1

print(happiness)
