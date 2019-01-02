
from random import randint, random
print(random())

i = 0
for trials in range(0,9999):
    ''' Region 1 result '''
    reg1 = random()
    if reg1 > 0.83:
        reg1 = 0
    else:
        reg1 = 1
    ''' Region 2 result '''        
    reg2 = random()
    if reg2 > 0.65:
        reg2 = 0
    else:
        reg2 = 1
    ''' Region 3 result '''            
    reg3 = random()
    if reg3 > 0.17:
        reg3 = 0
    else:
        reg3 = 1
    ''' If candidate A gets more than two regions they win '''
    if reg1 + reg2 + reg3 >= 2:
        i = i + 1

print("Total = ", i)
print("Average = ", i/10000)
