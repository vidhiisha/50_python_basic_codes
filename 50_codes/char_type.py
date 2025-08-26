def char_type(c):
    if c.isalpha(): return 'Alphabet'
    elif c.isdigit(): return 'Digit'
    else: return 'Special'

print(char_type(input()))