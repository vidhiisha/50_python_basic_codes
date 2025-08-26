def even_odd(lst):
    even=[lst[i] for i in range(0,len(lst),2)]
    odd=[lst[i] for i in range(1,len(lst),2)]
    return even,odd

lst=list(map(int,input().split()))
print(even_odd(lst))