from random import uniform

count = 0
run = 1000000
for i in range(run):
    if (uniform(0, 1)**2 + uniform(0, 1)**2) <= 1:
        count += 1
'''
count/run = area of quarter circle/area of square
or
count/run = (π(1)^2/4)/(1)^2 = π/4
'''
print(4*count/run)