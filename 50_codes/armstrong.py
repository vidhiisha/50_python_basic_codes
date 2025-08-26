def is_armstrong(num):
    order = len(str(num))
    return num == sum(int(d) ** order for d in str(num))

n = int(input("Enter a number: "))
print("Armstrong:", is_armstrong(n))