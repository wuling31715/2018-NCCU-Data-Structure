
import random

r = random.random() 
r = str(r)
r = r.replace('.', '')
r = r[:10]
big = r * (10 ** 5)
f = open('data', 'r+')
f.write(big)


f= open('data', 'r+')
r = f.read()
print(len(r))
