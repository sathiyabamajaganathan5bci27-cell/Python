from itertools import combinations_with_replacement

# Read input and split into string S and integer k
s, k = input().split()

# Sort the string and convert k to an integer
s_sorted = sorted(s)
k = int(k)

# Generate combinations with replacement of size k
for comb in combinations_with_replacement(s_sorted, k):
    # Join the tuple into a string and print
    print("".join(comb))
