#Pattern-1
'''
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
'''
n=9
for i in range(n+1):
    print(n*'* ')
print('\n\n')


#Pattern-2
'''
* * * * * * * * *
*               *
*               *
*               *
*               *
*               *
*               *
*               *
* * * * * * * * *
'''
n=9
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
* * * * * * *
* * * * * * * *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print(i*'* ')
print('\n\n')


#Pattern-4
'''
*
* *
*   *
*     *
*       *
*         *
*           *
*             *
* * * * * * * * *
'''
n=9
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
    * * * * * * *
  * * * * * * * *
* * * * * * * * *
'''
n=9
for i,j in zip(range (1,n+1,1), range (n-1,-1,-1)):
    print(j*'  '+i*'* ')
print('\n\n')


#Pattern-6
'''
                *
              * *
            *   *
          *     *
        *       *
      *         *
    *           *
  *             *
* * * * * * * * *
'''
n=9
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
* * * * * * * * *
  * * * * * * * *
    * * * * * * *
      * * * * * *
        * * * * *
          * * * *
            * * *
              * *
                *
'''
n=9
for i,j in zip(range (n,0,-1), range (0,n,1)):
    print(j*'  '+i*'* ')
print('\n\n')


#Pattern-8
'''
* * * * * * * * *
  *             * 
    *           *
      *         *
        *       *
          *     *
            *   *
              * *
                *
'''
n=9
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
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
n=9
for i in range (n,0,-1):
    print(i*'* ')
print('\n\n')


#Pattern-10
'''
* * * * * * * * *
*             *
*           *
*         *
*       *
*     *
*   *
* *
*
'''
n=9
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
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n=9
for i,j in zip(range (1,n+1,2), range ((n-1)//2,-1,-1)):
        print(j*'  '+i*'* ')
print('\n\n')


#Pattern-12
'''
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''
n=9
for i in range (1,(n+3)//2,1):
    print()
    for j in range (1,n+1,1):
        if j==(n+1)//2-i+1 or j==(n+1)//2+i-1 or i==(n+1)//2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-13
'''
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
n=9
x=0
for i in range (1,n+1,1):
    if i<=(n+1)//2:
        x+=1
    else:
        x-=1
    print(x*'* ')
print('\n\n')


#Pattern-14
'''
*
* * 
*   *
*     *
*       *
*     *
*   *
* *
*
'''
n=9
x=-1
print('*')
for i in range (1,n-1,1):
    if i<=(n-1)//2:
        x+=1
    else:
        x-=1
    print('* '+x*'  '+'* ')
print('*')
print('\n\n')    


#Pattern-15
'''
        *
      * * 
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i<=(n+1)//2:
        x+=1
    else:
        x-=1
    print(((n+1)//2-x)*'  '+x*'* ')
print('\n\n')


#Pattern-16
'''
        * 
      * *
    *   *
  *     *
*       *
  *     *
    *   *
      * *
        *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range ((n+1)//2,0,-1):
        if (j==i and j<=(n+1)//2) or (j==n-i+1 and j<=(n+1)//2) or j==1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-17
'''
* * * * * * * * * 
  * * * * * * * 
    * * * * *
      * * *
        *
'''
n=9
for i,j in zip(range (n,0,-2), range (0,(n+1)//2,1)):
        print(j*'  '+i*'* ')
print('\n\n')


#Pattern-18
'''
* * * * * * * * * 
  *           *
    *       *
      *   *
        *
'''
n=9
for i in range ((n+1)//2,0,-1):
    print()
    for j in range (1,n+1,1):
        if j==(n+1)//2-i+1 or j==(n+1)//2+i-1 or i==(n+1)//2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-19
'''
*
  *
    *
      *
        * 
          *
            *
              *
                *
'''
n=9
for i in range (0,n,1):
    print(i*'  '+'* ')
print('\n\n')


#Pattern-20
'''
                *
              *
            * 
          *
        *
      *
    *
  *
*
'''
n=9
for i in range (n-1,-1,-1):
    print(i*'  '+'* ')
print('\n\n')


#Pattern-21
'''
* 
  * 
    *
      *
        *
      *
    *
  *
*
'''
n=9
x=-1
for i in range (1,n+1,1):
    if i<=(n+1)//2:
        x+=1
    else:
        x-=1
    print(x*'  '+'* ')
print('\n\n')


#Pattern-22
'''
        * 
      * 
    *
  *
*
  *
    *
      *
        *
'''
n=9
x=-1
for i in range (1,n+1,1):
    if i<=(n+1)//2:
        x+=1
    else:
        x-=1
    print(((n-1)//2-x)*'  '+'* ')
print('\n\n')


#Pattern-23
'''
        *
      *   *
    *       *
  *           *
*               *
'''
n=9
for i in range (1,(n+3)//2,1):
    print()
    for j in range (1,n+1,1):
        if j==(n+1)//2-i+1 or j==(n+1)//2+i-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-24
'''
*               * 
  *           *
    *       *
      *   *
        *
'''
n=9
for i in range (1,(n+3)//2,1):
    print()
    for j in range (1,n+1,1):
        if j==n-i+1 or j==i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-25
'''
*               * 
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==n-i+1 or j==i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-26
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if (n+1)//2-x+1 <= j <= (n+1)//2+x-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-27
'''
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if j == (n+1)//2-x+1 or j == (n+1)//2+x-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-28
'''
* * * * * * * * * 
* * * *   * * * *
* * *       * * *
* *           * *
*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * *
'''
n=9
x=-1
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if (n+1)//2-x+1 <= j <= (n+1)//2+x-1:
            print(' ', end=' ')
        else:
            print('*', end=' ')
print('\n\n')


#Pattern-29
'''
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if x <= j <= n-x+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-30
'''
* * * * * * * * * 
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if x == j or j == n-x+1 or i==1 or i==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-31
'''
*               * 
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
'''
n=9
x=1
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if x <= j <= n-x+1:
            print(' ', end=' ')
        else:
            print('*', end=' ')
print('\n\n')


#Pattern-32
'''
*               * 
* *           * *
*   *       *   *
*     *   *     *
*       *       *
*     *   *     *
*   *       *   *
* *           * *
*               *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if j == x or j == n-x+1 or j==1 or j==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-33
'''
*  *  *  *  *  *  *  *  *  
*  *  *  *     *  *  *  *
*  *  *           *  *  *
*  *                 *  *
*                       *
'''
n=9
for i in range(1, (n+3)//2, 1):
    print()
    for j in range (1, n+1, 1):
        if (n+1)//2-i+2 <= j <= (n+1)//2+i-2:
            print('  ', end=' ')
        else:
            print('* ', end=' ')
print('\n\n')


#Pattern-34
'''
*                       *  
*  *                 *  *
*  *  *           *  *  *
*  *  *  *     *  *  *  *
*  *  *  *  *  *  *  *  *
'''
n=9
for i in range(1, (n+3)//2, 1):
    print()
    for j in range (1, n+1, 1):
        if i+1 <= j <= n-i:
            print('  ', end=' ')
        else:
            print('* ', end=' ')
print('\n\n')


#Pattern-35
'''
        *                 * 
      * * *             * * * 
    * * * * *         * * * * *     
  * * * * * * *     * * * * * * *   
* * * * * * * * * * * * * * * * * *
'''
n=9
for i,j in zip(range (1,n+1,2), range ((n-1)//2,-1,-1)):
        print(j*'  '+i*'* '+2 *j *'  '+i*'* ')
print('\n\n')


#Pattern-36
'''
* * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * *
'''
n=9
print(2*n*'* ')
print(2*n*'* ')
print('\n\n')


#Pattern-37
'''
        *
       * *
      *   *
     *     *
    *********
   *         *
  *           *
 *             *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,2*n+1,1):
        if j==n-i+1 or j==n+i-1 or (i==(n+1)//2 and n-i+2 <= j <= n+i-1):
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-38
'''
******** 
*       *
*       *
*       *
*********
*       *
*       *
*       *
********
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or (j==n and 1< i <n) or ((i==n or i==1) and j<n) or i==(n+1)//2:
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-39
'''
*********
*
*
*
*
*
*
*        
*********
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or i==1 or i==n:
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-40
'''
* * 
*  * 
*   *
*    *
*     *
*    *
*   *
*  *
* *
'''
n=9
x=-1
for i in range (1,n+1,1):
    if i<=(n+1)//2:
        x+=1
    else:
        x-=1
    print('* '+x*' '+'* ')
print('\n\n')


#Pattern-41
'''
*********
*
*
*
*********
*
*
*
*********
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or i==1 or i==n or i==(n+1)//2:
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-42
'''
*********
*
*
*
*********
*
*
*
*
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or i==1 or i==(n+1)//2:
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-43
'''
*********
*
*
*        
*   *****
*       *
*       *
*       *
*********
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or i==1 or i==n or (i==(n+1)//2 and j>=i) or (j==n and i>=(n+1)//2):
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-44
'''
*               * 
*               *
*               *
*               * 
* * * * * * * * *
*               *
*               *
*               *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or j==n or i==(n+1)//2:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-45
'''
* * * * * * * * * 
        *
        *
        *
        *
        *
        *
        *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or i==n or j==(n+1)//2:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-46
'''
* * * * * * * * * 
        *
        *
        *
        *
        *
        *
        *
* * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or (i==n and j<(n+1)//2) or (j==(n+1)//2 and i<n):
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-47
'''
*         * 
*       * 
*     *
*   *
* * 
*   *
*     *
*       *
*         *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i<=(n+1)//2:
        x+=1
    else:
        x-=1
    print('* '+((n+1)//2-x)*'  '+'* ')
print('\n\n')


#Pattern-48
'''
*        
*
*
*        
*
*
*
*
*********
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or j==1:
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-49
'''
*               * 
* *           * *
*   *       *   *
*     *   *     *
*       *       *
*               *
*               *
*               *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==n or j==1 or ((j==i or j==n-i+1) and i<=(n+1)//2):
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-50
'''
*               * 
* *             *
*   *           *
*     *         *
*       *       *
*         *     *
*           *   *
*             * *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==n or j==1 or j==i:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-51
'''
  * * * * * * *   
*               *
*               *
*               *
*               *
*               *
*               *
*               *
  * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if (j==1 and 1<i<n) or (j==n and 1<i<n) or (i==1 and 1<j<n) or (i==n and 1<j<n):
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-52
'''
* * * * * * * * *
*               *
*               *
*               *
* * * * * * * * *
*
*
*
*
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==1 or i==1 or i==(n+1)//2 or (j==n and i<=(n+1)//2):
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-53
'''
  * * * * * * *   
*               *
*               *
*               *
*       *       *
*         *     *
*           *   *
*             * *
  * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if (j==1 and 1<i<n) or (j==n and 1<i<n) or (i==1 and 1<j<n) or (i==n and 1<j<n) or (i==j and i>=(n+1)//2):
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-54
'''
* * * * * 
*       *
*       *
*       *
* * * * *
* *
*   *
*     *
*       *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,(n+3)//2,1):
        if j==1 or i==1 or i==(n+1)//2 or (j==(n+1)//2 and i<=(n+1)//2) or j==i-(n+1)//2+1:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-55
'''
* * * * * * * * * 
*
*
*
* * * * * * * * *
                *
                *
                *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or i==1 or i==(n+1)//2 or (j==1 and i<=(n+1)//2) or (j==n and i>=(n+1)//2):
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-56
'''
* * * * * * * * * 
        *
        *
        *
        *
        *
        *
        *
        *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or j==(n+1)//2:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-57
'''
*               * 
*               *
*               *
*               *
*               *
*               *
*               *
*               *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or j==1 or j==n:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-58
'''
*               * 
 *             *
  *           *
   *         *
    *       *
     *     *
      *   *
       * *
        *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,2*n+1,1):
        if j==i or j==2*n-i:
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-59
'''
*       *       * 
*      * *      *
*     *   *     *
*    *     *    *
*   *       *   *
*  *         *  *
* *           * *
**             **
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,2*n+1,1):
        if j==n-i+1 or j==n+i-1 or j==1 or j==2*n-1:
            print('*', end='')
        else:
            print(' ', end='')
print('\n\n')


#Pattern-60
'''
*               * 
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==n-i+1 or j==i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-61
'''
*               *
  *           *
    *       *
      *   *
        *
        *
        *
        *
        *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if (j==i and i<=(n+1)//2) or (j==n-i+1 and i<=(n+1)//2) or (j==(n+1)//2 and i>=(n+1)//2):
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-62
'''
* * * * * * * * * 
              *
            *
          *
        *
      *
    *
  *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or i==n or j==n-i+1:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-63
'''
*       *       * 
  *     *     *
    *   *   *
      * * *
* * * * * * * * *
      * * *
    *   *   *
  *     *     *
*       *       *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j==i or j==n-i+1 or i==(n+1)//2 or j==(n+1)//2:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-64
'''
  *   *   *   *   
*   *   *   *   *
  *   *   *   *
*   *   *   *   *
  *   *   *   *
*   *   *   *   * 
  *   *   *   *   
*   *   *   *   *
  *   *   *   *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if (i+j)%2==1:
            print('* ', end='')
        else:
            print('  ', end='')
print('\n\n')


#Pattern-65
'''
* * * * * * * * * 
*               *
*   * * * * *   *
*   *       *   * 
*   *   *   *   *
*   *       *   *
*   * * * * *   *
*               *
* * * * * * * * *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if (not (x<j<n-x+1) and j%2==1) or(x<=j<=n-x+1 and i%2==1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-66
'''
* * * * *       * 
        *       *
        *       *
        *       *
* * * * * * * * *
*       *
*       *
*       *
*       * * * * *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if i==(n+1)//2 or j==(n+1)//2 or (i==1 and j<=(n+1)//2) or (i==n and j>=(n+1)//2) or (j==1 and i>=(n+1)//2) or (j==n and i<=(n+1)//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-67
'''
        * *
        * *
    * * * * * *
    * * * * * *
* * * * * * * * * *
'''
n=11
x=-1
for i in range (1,n//2+1,1):
    if i%2==1:
        x+=2
    print()
    for j in range (1,n+1,1):
        if n//2-x+1 <= j <= n//2+x:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-68
'''
        * *
        * *
    *         *
    *         *
*                 *
'''
n=11
x=-1
for i in range (1,n//2+1,1):
    if i%2==1:
        x+=2
    print()
    for j in range (1,n+1,1):
        if n//2-x+1 == j or j == n//2+x:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-69
'''
        *
          *
            *
              *
* * * * * * * * *
              *
            *
          *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if i==(n+1)//2 or j==(n+1)//2+x-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-70
'''
        *
      *
    *
  *
* * * * * * * * *
  *
    *
      *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if i==(n+1)//2 or j==(n+1)//2-x+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-71
'''
        *
      * * *
    *   *   *
  *     *     *
*       *       *
        *
        *
        *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    print()
    for j in range (1,n+1,1):
        if j==(n+1)//2 or ((j==(n+1)//2-x+1 or j==(n+1)//2+x-1) and i<=(n+1)//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-72
'''
        *
        *
        *
        *
*       *       *
  *     *     *
    *   *   *
      * * *
        *
'''
n=9
x=(n+3)//2
for i in range (1,n+1,1):
    if i >= (n+1)//2:
        x-=1
    print()
    for j in range (1,n+1,1):
        if j==(n+1)//2 or ((j==(n+1)//2-x+1 or j==(n+1)//2+x-1) and i>=(n+1)//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-73
'''
        *
        * *
        * * *
        * * * *
* * * * * * * * *
        * * * *
        * * *
        * *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if i==(n+1)//2 or (n+1)//2<=j<=(n+1)//2+x-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-74
'''
        *
      * *
    * * *
  * * * *
* * * * * * * * *
  * * * *
    * * *
      * *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    else:
        x-=1
    print()
    for j in range (1,n+1,1):
        if i==(n+1)//2 or (n+1)//2>=j>=(n+1)//2-x+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-75
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
        *
        *
        *
        *
'''
n=9
x=0
for i in range (1,n+1,1):
    if i <= (n+1)//2:
        x+=1
    print()
    for j in range (1,n+1,1):
        if j==(n+1)//2 or (((n+1)//2-x+1<=j<=(n+1)//2+x-1) and i<=(n+1)//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-76
'''
        *
        *
        *
        *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=9
x=(n+3)//2
for i in range (1,n+1,1):
    if i >= (n+1)//2:
        x-=1
    print()
    for j in range (1,n+1,1):
        if j==(n+1)//2 or (((n+1)//2-x+1<=j<=(n+1)//2+x-1) and i>=(n+1)//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-77
'''
* * * * * * * * * 
* *
*   *
*     *
*       *
*         *
*           *
*             *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or j==1 or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-78
'''
* * * * * * * * * 
              * *
            *   *
          *     *
        *       *
      *         *
    *           *
  *             *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or j==n or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-79
'''
*               * 
  *             *
    *           *
      *         *
        *       *
          *     *
            *   *
              * *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or j==n or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-80
'''
*               * 
*             *
*           *
*         *
*       *
*     *
*   *
* *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or j==1 or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-81
'''
* * * * * * * * * 
* *           *
*   *       *     
*     *   *
*       *
*     *   *
*   *       *
* *           *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or j==1 or i==j or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-82
'''
* * * * * * * * * 
  *           * *
    *       *   *
      *   *     *
        *       *
      *   *     *
    *       *   *
  *           * *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==1 or j==n or i==j or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-83
'''
*               * 
  *           * *
    *       *   *
      *   *     *
        *       *
      *   *     *
    *       *   *
  *           * *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or j==n or i==j or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-84
'''
*               * 
* *           *
*   *       *
*     *   *
*       *
*     *   *
*   *       *
* *           *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or j==1 or i==j or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-85
'''
* * * * * * * * * 
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *   *
* * *       *
* *           *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j<=n-i+1 or j==i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-86
'''
* * * * * * * * * 
  * * * * * * * *
    * * * * * * *
      * * * * * *
        * * * * *
      *   * * * *
    *       * * *
  *           * *
*               *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j>=i or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-87
'''
*               * 
  *           * *
    *       * * *
      *   * * * *
        * * * * *
      * * * * * *
    * * * * * * *
  * * * * * * * *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j>=n-i+1 or j==i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-88
'''
*               * 
* *           *
* * *       *
* * * *   *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if j<=i or j==n-i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-89
'''
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
* * * * * * * * *
*               *
*               *
*               *
* * * * * * * * *
'''
n=9
for i in range (1,n+1,1):
    print()
    for j in range (1,n+1,1):
        if i==n or j==1 or j==n or i==(n+1)//2 or (j%2==1 and i<=(n+1)//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print('\n\n')


#Pattern-90
'''
                    ****
            ********************
        ****************************
      ********************************
    ************************************
    ************************************
  ****************************************
  ****************************************
  ****************************************
  ****************************************
  ****************************************
  ****************************************
    ************************************
    ************************************
      ********************************
        ****************************
            ********************
                    ****
'''
n=100
a=10
for i in range (a,1,-1):
    x=int((n-i**2)**0.5)
    print((a-x)*'  '+4*(x+1)*'*')
for i in range (2,a+1):
    x=int((n-i**2)**0.5)
    print((a-x)*'  '+4*(x+1)*'*')
print('\n\n')


#Pattern-91
'''
                             *
                             *
                             *
             *               *
     *       *           *   *
     *       *           *   *       *
 *   *       *       *   *   *       *
 *   *       *       *   *   *       *
 *   *       *   *   *   *   *       *
 *   *       *   *   *   *   *       *
 *   *   *   *   *   *   *   *       *
 *   *   *   *   *   *   *   *   *   *
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9]
'''
m = int(input('Enter total number of entities: '))
print('Enter the max values: ')
n = [int(input()) for i in range (m)]
for i in range(max(n),0,-1):
    for j in range(0,m):
        if i<=n[j]:
            print(' *  ', end='')
        else:
            print('    ', end='')
    print()

for i in range (1,m+1):
    print(f'[{i}] ', end='')
print('\n\n')


#Pattern-92
'''
        *                 *                 *
      * * *             * * *             * * *       
    * * * * *         * * * * *         * * * * *
  * * * * * * *     * * * * * * *     * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * *
'''
n=5
b=3
for i in range (1,n+1):
    print(b*((n-i)*'  '+(2*i-1)*'* '+(n-i)*'  '))
print('\n\n')


#Pattern-93
'''
        *                   *                   *
      *   *               *   *               *   *
    *       *           *       *           *       *
  *           *       *           *       *           *   
*               *   *               *   *               *
'''
n=5
b=3
k=5
for i in range (1,n+1):
    print()
    for j in range (1, b*2*n):
        if j%10==k or j%10==5+i-1:
            print('* ', end='')
        else:
            print('  ', end='')
    k-=1
print('\n\n')

