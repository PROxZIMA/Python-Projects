print('Operations performed here are addition(add), subtraction(sub), multiplication(mult), division(div), exponential(exp), factorial(fact)')
#Addition
def add():
	L=[]
	b=0
	num=int(input("Enter how many numbers you are adding : "))
	for n in range(num):
	    N=float(input("Enter the numbers : "))
	    L.append(N)
	    b=b+N
	print('Summation of the numbers is =',b)
#Subtraction
def sub():
	a=float(input('Enter 1st number : '))
	b=float(input('Enter 2nd number : '))
	print('Subtraction of the number is =',a-b)
#Multiplication
def mult():
	L=[]
	b=1
	num=int(input("Enter how many numbers you are multiplying : "))
	for i in range(num):
	    n=float(input("Enter the numbers : "))
	    L.append(n)
	    b=b*n
	print('Multiplication of the numbers is =',b)
#Division
def div():
	a=float(input('Enter Numerator : '))
	b=float(input('Enter Denominator : '))
	print('Exact division is =',a/b)
	print('Integral value of division is =',a//b)
	print('Remainder after division is =',a%b)
#Exponential
def exp():
	a=float(input('Enter Base : '))
	b=float(input('Enter Power : '))
	print('Exponential is given by =',a**b)
#Factorial
def fact():
	b=1
	n=int(input('Enter a integer for its factorial : '))
	print('Factorial is also represented by :',end=' ')
	for i in range(n,0,-1):
		b*=i
		print(i,'*',end=' ')
	print('\nFactorial of the number is =',n,'! =',b)
#Defination ending
try:
	opt=input('\nEnter operator keyword you want to perform : ')
	while 1:
		if opt=='add':
			add()
		elif opt=='sub':
			sub()
		elif opt=='mult':
			mult()
		elif opt=='div':
			div()
		elif opt=='exp':
			exp()
		elif opt=='fact':
			fact()
		else:
			print('Enter correct operator keyword')
		opt_2=input('\nEnter an operator keyword again (enter 0 to stop) : ')
		if opt_2=='0':
			break
		opt=opt_2
except ValueError:
	print('Enter number or \'0\' only')