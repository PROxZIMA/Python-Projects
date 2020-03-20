print('An Armstrong number is an integer with \'n\' digits such that the sum of \'nth\' power of it\'s digits is equal to the number itself.')
a=input('Enter any number : ')
sum=0
for i in a:
	sum+=int(i)**len(a)
if sum==int(a):
	print('It is an Armstrong number')
else:
	print('It\'s not an Armstrong Number')