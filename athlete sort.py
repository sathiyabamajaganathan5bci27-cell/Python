# Read N (athletes) and M (attributes)
n, m = map(int, input().split())

# Read the athlete data into a list of lists
athletes = []
for _ in range(n):
    athletes.append(list(map(int, input().split())))

# Read the attribute index K to sort by
k = int(input())

# Sort using a lambda function that looks at index K
# Python's sort is stable, so original order is kept for ties
athletes.sort(key=lambda x: x[k])

# Print the resulting table
for athlete in athletes:
    print(*(athlete))
