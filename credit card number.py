import re

# Step 1: Define the structural regex
# ^[456] : Starts with 4, 5, or 6
# \d{3} : Followed by 3 digits (total 4)
# (-?\d{4}){3} : Followed by 3 groups of (optional hyphen + 4 digits)
# $ : End of string
regex_structure = r"^[456]\d{3}(-?\d{4}){3}$"

# Step 2: Define the repeated digits check
# This looks for any digit (\d) followed by itself 3 more times (\1{3})
regex_repeat = r"(\d)\1{3,}"

n = int(input())

for _ in range(n):
    card = input().strip()
    
    # Check basic structure first
    if re.match(regex_structure, card):
        # Remove hyphens to check for consecutive repeated digits across groups
        card_digits = card.replace("-", "")
        
        if re.search(regex_repeat, card_digits):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
