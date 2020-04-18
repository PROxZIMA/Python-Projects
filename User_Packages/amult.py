def mult():
	L=[]
	b=1
	num=int(input("Enter how many numbers you are multiplying : "))
	for i in range(num):
	    n=float(input("Enter the numbers : "))
	    L.append(n)
	    b=b*n
	print('Multiplication of the numbers is =',b)