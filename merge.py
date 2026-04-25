def merge_the_tools(string, k):
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        t = string[i:i+k]
        u = ""
        # Build string u by checking for existing characters to maintain order
        for char in t:
            if char not in u:
                u += char
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
