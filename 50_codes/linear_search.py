def linear_search(arr,x):
    for i,val in enumerate(arr):
        if val==x: return i
    return -1

arr=list(map(int,input().split()))
x=int(input())
print(linear_search(arr,x))