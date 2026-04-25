from itertools import combinations

# Read input
n = int(input())
letters = input().split()
k = int(input())

# Generate all possible combinations of indices
# We use indices (0 to n-1) to handle duplicate letters correctly
all_combinations = list(combinations(range(n), k))

# Filter combinations that contain at least one index where letters[index] == 'a'
contains_a = [c for c in all_combinations if any(letters[i] == 'a' for i in c)]

# Calculate and print probability
probability = len(contains_a) / len(all_combinations)
print(f"{probability:.4f}")
