import re

# N = rows, M = columns
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# Step 1: Read the matrix column-wise to get the encoded string
# This uses the 'zip' trick to transpose rows into columns
encoded_string = "".join(["".join(column) for column in zip(*matrix)])

# Step 2: Use a "Lookbehind" and "Lookahead" regex
# It finds symbols (!@#$%) only if they are between alphanumeric characters (\w)
decoded_string = re.sub(r'(?<=\w)([^\w\s]+)(?=\w)', ' ', encoded_string)

print(decoded_string)
