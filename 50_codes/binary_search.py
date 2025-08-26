def binary_search(arr,x):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x: return mid
        elif arr[mid]<x: low=mid+1
        else: high=mid-1
    return -1

arr=sorted(list(map(int,input().split())))
x=int(input())
print(binary_search(arr,x))