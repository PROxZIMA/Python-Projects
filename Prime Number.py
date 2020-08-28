import timeit
setup = 'from math import sqrt'

code = '''
def prime():
    p = 99999989
    # p = int(input('Enter a number : '))
    if p <= 1:
        return False

    elif p <= 3:
        return True

    elif p % 2 == 0 or p % 3 == 0:
        return False

    else:
        for i in range (5, int(sqrt(p)) + 1, 6):
            if p % i == 0 or p % (i + 2) == 0:
                return False
        else:
            return True
'''
# print(prime())

print(timeit.timeit(setup = setup, stmt = code, number = 1000000))