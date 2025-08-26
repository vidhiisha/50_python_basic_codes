import math

def gcd(a,b):
    return math.gcd(a,b)

x,y = map(int, input("Enter two numbers: ").split())
print("GCD:", gcd(x,y))