def prime_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

num = int(input("Enter a number: "))
print("Prime factors:", prime_factors(num))