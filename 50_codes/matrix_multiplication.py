def multiply_matrices(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

m,n=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(m)]
p,q=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(p)]
print(multiply_matrices(A,B))