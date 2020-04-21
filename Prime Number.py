import timeit

def prime():
    p=99999989
    # p=int(input('Enter a number : '))
    if p==1:
        pass
        # print('1 is a uniqe number')
    elif p%2==0:
        pass
        # print('Not a Prime Number')
    elif p%3==0:
        pass
        # print('Not a Prime Number')
    elif p%3!=0:
        for i in range (5,int(p**0.5),6):
            if p%i==0 or p%(i+2)==0:
                pass
                # print('Not a Prime number')
                # break
        else:
            return p
            # print('Prime number found')

print(min(timeit.Timer(prime).repeat(10, 1000)))