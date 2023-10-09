def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def desiredArray(K,N,Arr):
    lcm_value=1
    for num in Arr:
        lcm_value=lcm(lcm_value,num)
    non_divisble_integers=[]
    num=1
    while len(non_divisble_integers)<K:
        divisible=False
        for divisor in Arr:
            if num % divisor ==0:
                divisible =True 
                break
        if not divisible:
            non_divisble_integers.append(num)
        num=+1
    total_sum=sum(non_divisble_integers)

    return total_sum

K=4
N=6
Arr=[4,8,16]

print(desiredArray(K,N,Arr))