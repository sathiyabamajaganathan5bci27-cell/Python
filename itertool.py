from itertools import product

if __name__ == '__main__':
    # Read the two lists and convert them to integers
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Compute the cartesian product
    result = product(A, B)
    
    # Print the tuples separated by a space
    print(*result)
