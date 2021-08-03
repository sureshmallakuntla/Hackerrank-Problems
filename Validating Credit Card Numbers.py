# Validation of Credit Card
import re
for _ in range(int(input())):
    s=input().strip()
    if not re.search("^[456]\d{3}(-?\d{4}){3}$",s) or re.search(r"(\d)\1{3}", re.sub("-", "",s)):
        print('Invalid')
    else:
        print('Valid')
