def myfunc(n):
    return lambda a: a*n
ans=myfunc(6)
print(ans(10))