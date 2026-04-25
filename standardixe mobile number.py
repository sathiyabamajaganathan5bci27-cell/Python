def wrapper(f):
    def fun(l):
        # Format logic: take last 10 digits and add prefix
        standardized = []
        for num in l:
            clean_num = num[-10:]
            standardized.append(f"+91 {clean_num[:5]} {clean_num[5:]}")
        # Call the original sort function with standardized numbers
        return f(standardized)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
