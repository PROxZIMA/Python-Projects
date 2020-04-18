n = int(input('Enter how many number in Fibonacci Series you want: '))
a, b = 0, 1
print(f'Fibonacci Series is given by: ')
for i in range (1, n+1):
    if i == n:
        print(b)
    else:
        print(f'{b}, ', end='')
    a, b = b, a+b