# Read first set input
m = int(input())
set_a = set(map(int, input().split()))

# Read second set input
n = int(input())
set_b = set(map(int, input().split()))

# Calculate symmetric difference
# This finds elements in (a - b) and (b - a)
diff = set_a.symmetric_difference(set_b)

# Sort the resulting set and print each element on a new line
for val in sorted(diff):
    print(val)
