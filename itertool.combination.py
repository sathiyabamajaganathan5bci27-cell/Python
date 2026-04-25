from itertools import combinations

# Read input and split into string S and integer k
s, k = input().split()
k = int(k)

# Sort the string lexicographically to ensure combinations are in order
s_sorted = sorted(s)

# Loop through each size from 1 to k (inclusive)
for i in range(1, k + 1):
    # Generate all combinations of length i
    for comb in combinations(s_sorted, i):
        # Join the tuple into a string and print
        print("".join(comb))
