def transpose_matrix(M):
    return list(map(list,zip(*M)))

m,n=map(int,input().split())
M=[list(map(int,input().split())) for _ in range(m)]
print(transpose_matrix(M))