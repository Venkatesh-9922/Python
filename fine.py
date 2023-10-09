def Finenumber(a,b):
    if not a or not b:
        return None
    
    ans=0
    for num_a in a:
        for num_b in b:
            d=abs(num_a-num_b)
            ans=max(ans,d)
    return ans

a,b=1,3
print(Finenumber)
