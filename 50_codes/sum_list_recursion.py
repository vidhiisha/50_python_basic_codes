def sum_list(lst):
    if not lst: return 0
    return lst[0]+sum_list(lst[1:])

lst=list(map(int,input().split()))
print(sum_list(lst))