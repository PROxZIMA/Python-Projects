print('An Armstrong number is an integer with \'n\' digits such that the sum of \'nth\' power of it\'s digits is equal to the number itself.')
a=int(input('Enter any number : '))
n=str(a)
sum=0
for i in n:
	sum=sum+int(i)**len(n)
if sum==a:
	print('It is an Armstrong number')
else:
	print('It\'s not an Armstrong Number')