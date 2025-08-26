def is_symmetric(matrix):
    return matrix == [list(row) for row in zip(*matrix)]

size=int(input("Enter size of square matrix: "))
matrix=[list(map(int,input().split())) for _ in range(size)]
print(is_symmetric(matrix))