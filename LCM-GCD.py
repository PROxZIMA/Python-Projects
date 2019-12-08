#least Common Multiple
def LCM(n1,n2):
    for i in range(max(n1,n2),(n1*n2)+1,max(n1,n2)):
        if i%n1==0 and i%n2==0:
            print('\nLeast Common Multiple (L.C.M) of',n1,'and',n2,'is =',i)
            return
    print('No L.C.M found')
#Greatest Common Diviser
def GCD(n1,n2):
    for i in range(min(n1,n2),0,-1):
        if n1%i==0 and n2%i==0:
            print('Greatest Common Diviser (G.C.D) of',n1,'and',n2,'is =',i)
            return
    print('No G.C.D found')
try:
    n1=int(input('Enter first number : '))
    n2=int(input('Enter second number : '))
    LCM(n1,n2)
    GCD(n1,n2)
except ValueError:
    print('Enter a number please')