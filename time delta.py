from datetime import datetime

def time_delta(t1, t2):
    # Format: Day dd Mon yyyy hh:mm:ss +xxxx
    fmt = '%a %d %b %Y %H:%M:%S %z'
    
    # Convert strings to datetime objects
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    # Calculate the absolute difference in seconds
    diff = int(abs((dt1 - dt2).total_seconds()))
    return str(diff)

# Process test cases
t = int(input())
for _ in range(t):
    t1 = input()
    t2 = input()
    print(time_delta(t1, t2))
