n=int(input('Enter a number below which you want Prime Numbers : '))
print ('\nPrime Numbers below',n,'are given by :')
print('1 is a unique number')
for p in range(3,n+1):
	if p%2==0:
		pass
	elif p%2!=0:
		for i in range (3,((p+1)//2),2):
			if p%i==0:
				break
		else:
			print(p)