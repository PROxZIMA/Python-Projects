def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n = int(input('Enter table height: '))

for i in range (0, n):
    print()
    for j in range (0, i+1):
        print(fact(i)//(fact(j)*fact(i-j)), ' ', end='')