#Pattern-1
'''
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
'''
n=6
for i in range(1,n+1,1):
    print()
    for j in range(1,n+1,1):
        print('*',end=' ')
print('\n\n')


#Pattern-2
'''
* * * * * *
*         *
*         *
*         *
*         *
* * * * * *
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or j==n or i==1 or i==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-3
'''
*
* *
* * *
* * * *
* * * * *
* * * * * *
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,i+1,1):
        print('*', end=' ')
print('\n\n')


#Pattern-4
'''
*
* *
*   *
*     *
*       *
* * * * * *
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,i+1,1):
        if i==1 or i==n or j==1 or j==i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-5
'''
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j>n-i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-6
'''
          *
        * *
      *   *
    *     *
  *       *
* * * * * *
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==n-i+1 or j==n or i==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-7
'''
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j>i-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-8
'''
* * * * * *
  *       *
    *     *
      *   *
        * *
          *
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==i or j==n or i==1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-9
'''
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j<n-i+2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-10
'''
* * * * * *
*       *
*     *
*   *
* *
*
'''
n=6
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==n-i+1 or j==1 or i==1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-11
'''
    *
   ***
  *****
 *******
*********
'''
n=9
for i,j in zip(range (1,n+1,2), range ((n-1)//2,-1,-1)):
		print(j*' ',i*'*')
print('\n\n')


#Pattern-12
