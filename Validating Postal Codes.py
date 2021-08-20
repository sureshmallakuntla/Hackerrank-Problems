# Validating Postal Codes

import re
def validZipcode(s):
    return s.isdigit() and (len(s) == 6) and (s[0] != '0') and (alternative(s) <= 1)
    
def alternative(s):
    c = 0
    for i in range(4):
        c += (s[i] == s[i + 2])
    return c
    
s = input()
print(validZipcode(s))

P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
