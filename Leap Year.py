def leap(n):
    return n%4==0 and (n%400==0 or n%100!=0)

n = int(input('Check that a year is leap or not: '))
print(leap(n))