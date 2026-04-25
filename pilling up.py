from collections import deque

for _ in range(int(input())):
    n = int(input())
    # Use a deque for efficient O(1) popping from both ends
    blocks = deque(map(int, input().split()))
    
    last_picked = float('inf')
    possible = True
    
    while blocks:
        # Greedily pick the larger of the two ends
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.popright()
        
        # If the current block is bigger than the last one placed, it's impossible
        if current > last_picked:
            possible = False
            break
        last_picked = current
        
    print("Yes" if possible else "No")
