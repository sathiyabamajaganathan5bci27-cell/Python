from itertools import product

# Read K (number of lists) and M (modulo value)
k, m = map(int, input().split())

# Read each list, squaring the elements immediately and storing them
# We ignore the first element of each line (Ni) using [1:]
lists = []
for _ in range(k):
    row = list(map(int, input().split()))[1:]
    lists.append([x**2 for x in row])

# Use itertools.product to get every possible combination of picking one from each list
# Calculate the sum of each combination, take modulo M, and find the max
max_val = 0
for combination in product(*lists):
    current_sum = sum(combination) % m
    if current_sum > max_val:
        max_val = current_sum

print(max_val)
