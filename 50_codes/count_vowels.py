def count_vowels(s):
    return sum(c in "aeiouAEIOU" for c in s)

print(count_vowels(input()))