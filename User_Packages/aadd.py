def add():
	L=[]
	b=0
	num=int(input("Enter how many numbers you are adding : "))
	for n in range(num):
	    N=float(input("Enter the numbers : "))
	    L.append(N)
	    b=b+N
	print('Summation of the numbers is =',b)