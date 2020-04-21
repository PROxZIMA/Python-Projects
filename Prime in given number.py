import timeit

def prime():
    x=100000000
    # n=int(input('Enter a number below which you want Prime Numbers : '))
    # print (f'\nPrime Numbers below {n} are given by :')
    # print('1 is a unique number')
    for p in range(3,x+1):
        if p%2==0:
            pass
        elif p%3==0:
            pass
        elif p%3!=0:
            for i in range (5,int(p**0.5),6):
                if p%i==0 or p%(i+2)==0:
                    break
            else:
                return p

print(min(timeit.Timer(prime).repeat(10, 100000)))