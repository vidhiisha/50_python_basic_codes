def sum_digits(n):
    return sum(map(int, str(n)))

print(sum_digits(int(input("Enter a number: "))))