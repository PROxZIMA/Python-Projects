n=int(input('Enter number whose table you want : \n'))
while 1: #while 1: means an infinite loop because it's always true
#for x in range (1,999999,1): #also works as infinite loop
	for i in range (1,11):
		print(n,'×',i,'=',n*i)
	a=int(input('Enter a number for next table (enter 0 to stop) : \n'))
	if a==0:
		break;
	n=a