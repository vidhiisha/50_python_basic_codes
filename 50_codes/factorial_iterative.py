def factorial_iterative(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

print(factorial_iterative(int(input())))