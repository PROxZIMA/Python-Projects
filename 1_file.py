import random

adjs = ['nice', 'fine', 'good', 'bad', 'happy']
adj = random.choice(adjs)

nouns = ['pune', 'raman', 'sun', 'pratik', 'road']
noun = random.choice(nouns)

num = str(random.randrange(1, 100))

print('Your random password is :',adj+noun+num )
