import string
str=string.ascii_letters

#Prime Number
def prime(p):
	if p==1:
		print('1 is a uniqe number')
	elif p%2==0:
		print('Not a Prime Number')
	elif p%2!=0:
		for i in range (3,int(p**0.5),2):
			if p%i==0:
				print('Not a Prime number')
				break
		else:
			print('Prime number found')

#Factorial
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

#Prime Factor
def pfact(p):
    print('Prime factors =',end=' ')
    while p%2==0:
        print(2,end=' , ')
        p/=2
    for i in range (3,int(p**0.5),2):
        while p%i==0:
            print(i,end=' , ')
            p/=i
    if p>2:
        print(p)

p=int(input('Enter a number : '))
while 1:
	print('Square root of the number is =',p**0.5)
	print('Square of the number is =',p**2)
	print('Cube of the number is =',p**3)
	print(f'\nFactorial of the number is = {p}! = {fact(p)}')
	prime(p)
	pfact(p)
	def fun():
		fun.a=input('\nEnter a new number (enter 0 to stop) : ')
		if fun.a=='0':
			exit()
		elif (any(x in str for x in fun.a)):
			print('Enter a number or 0 only')
			fun()
	fun()
	p=int(fun.a)