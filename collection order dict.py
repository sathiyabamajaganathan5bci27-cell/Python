from collections import OrderedDict

# Initialize the ordered dictionary
items = OrderedDict()

# Read the number of items
n = int(input())

for _ in range(n):
    # Read input and split into item name and price
    # rpartition splits at the last space found
    data = input().rpartition(' ')
    item_name = data[0]
    net_price = int(data[2])
    
    # If item exists, add to existing price; otherwise, create it
    if item_name in items:
        items[item_name] += net_price
    else:
        items[item_name] = net_price

# Print the results in order of first occurrence
for name, price in items.items():
    print(f"{name} {price}")
