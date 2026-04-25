# Read the number of test cases
t = int(input())

for _ in range(t):
    try:
        # Read and split the input values
        a, b = input().split()
        # Perform integer division
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        # Print the error code as per requirements
        print("Error Code:", e)
