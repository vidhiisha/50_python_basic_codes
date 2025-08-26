def number_triangle(n):
    for i in range(1,n+1):
        print(' '.join(map(str,range(1,i+1))))

number_triangle(5)