import math

def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

x,y = map(int, input("Enter two numbers: ").split())
print("LCM:", lcm(x,y))