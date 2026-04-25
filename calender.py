import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    
    # weekday() returns 0 for Monday, 1 for Tuesday, etc.
    day_index = calendar.weekday(year, month, day)
    
    # Get the day name and convert to uppercase
    print(calendar.day_name[day_index].upper())
