D={'Name':'Pratik Pingale','Roll No.':'19CO 056','Division':'IV','Marks':90}
for x in D:
	print(x,':',D[x])
print('\n')
print('• City Updated')
D['City']='Pune'
for x in D:
	print(x,':',D[x])
print('\n')
print('• Roll No. deleted')
del D['Roll No.']
for x in D:
	print(x,':',D[x])