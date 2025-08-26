def sub_matrices(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

m,n=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(m)]
B=[list(map(int,input().split())) for _ in range(m)]
print(sub_matrices(A,B))