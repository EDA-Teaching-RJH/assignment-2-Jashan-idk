### Part Four -- your code goes here. 
import random

randomlist = []
for i in range(0,10):
    n = random.randint(1, 100)
    randomlist.append(n)
    

o = 0  
while o < len(randomlist):
    if randomlist[o] % 2 == 0:
        randomlist.pop(o)
    else:
        o = o + 1

print(randomlist)