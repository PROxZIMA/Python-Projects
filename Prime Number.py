import datetime

t0=datetime.datetime.now()

p=int(input('Enter a number : '))

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


t1=datetime.datetime.now()
print('Time taken = ', t1-t0)