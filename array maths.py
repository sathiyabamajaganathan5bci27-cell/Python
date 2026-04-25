import numpy

# Standardise NumPy print options to match HackerRank's legacy output style
numpy.set_printoptions(legacy='1.13')

# Read N and M
n, m = map(int, input().split())

# Read array A and array B
# We use a list comprehension to read N lines for each array
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

# Perform and print operations
print(a + b)
print(a - b)
print(a * b)
print(a // b) # Integer Division
print(a % b)
print(a ** b)
