from math import sqrt

def prime():
    n = int(input('Enter a number below which you want Prime Numbers : '))
    print(f'\nPrime Numbers below {n} are given by :\n1 is a unique number')

    print('2\n3')
    for p in range(5, n + 1, 2):
        if p % 3 == 0:
            continue
        else:
            for i in range (5, int(sqrt(p)) + 1, 6):
                if p % i == 0 or p % (i + 2) == 0:
                    break
            else:
                # return p
                print(p)
prime()