def max_list(lst):
    if len(lst)==1: return lst[0]
    m=max_list(lst[1:])
    return lst[0] if lst[0]>m else m

lst=list(map(int,input().split()))
print(max_list(lst))