
from random import randint
print (randint(1,6))


''' Finding the average of 10,000 rolss of a dice '''
i = 0
for trials in range(0,10000):
    j = (randint(1,6))
    i = i + j
print("Total = ", i)
print("Average = ", i/10000)

    
