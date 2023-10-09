num=int(input('Enter Number:'))
if num >1:
    for i in range(2,int(num/2)+1):
        if (num % i )==0:
            print('Not a Prime Number')
            break

    else:
        print("Prime Number")
else:
    print('Not a Prime Number')