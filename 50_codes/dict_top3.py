def top_three(d):
    return sorted(d.items(),key=lambda x:x[1],reverse=True)[:3]

D={'A':10,'B':2,'C':3,'D':6,'E':1}
print(top_three(D))