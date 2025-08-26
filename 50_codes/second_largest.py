def second_largest(lst):
    return sorted(lst,reverse=True)[1]

lst=list(map(int,input().split()))
print(second_largest(lst))