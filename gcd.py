def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a 
result=GCD(10,40)

print(result)