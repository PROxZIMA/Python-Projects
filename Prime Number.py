p=int(input('Enter a number : '))
if p==1:
	print('1 is a uniqe number')
elif p%2==0:
	print('Not a Prime Number')
elif p%2!=0:
	for i in range (3,((p+1)//2),2):
		if p%i==0:
			print('Not a Prime number')
			break
	else:
		print('Prime number found')