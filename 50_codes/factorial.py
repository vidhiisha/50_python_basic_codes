def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    return 1 if n == 0 else n * factorial(n-1)

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))