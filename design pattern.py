n, m = map(int, input().split())

# Top section: pattern increases by 2 each line
for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

# Middle section: WELCOME text
print("WELCOME".center(m, "-"))

# Bottom section: pattern decreases by 2 each line
for i in range(n-2, 0, -2):
    print((".|." * i).center(m, "-"))
