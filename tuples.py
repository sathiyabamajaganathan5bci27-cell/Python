if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    # Create the tuple from the mapped integers
    t = tuple(integer_list)
    
    # Compute and print the hash
    print(hash(t))
