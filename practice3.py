'''
for i in range(1,7):
    if i == 3:
        break
    print(i)

print("Finished with i = ", str(i))


for i in range(1,7):
    if i == 3:
        continue
    print(i)

print("Finished with i = ", str(i))

'''

letter_input = input("Guess a letter: ")
while True:
    ''' n.b. while True creates an infinite loop out of which I can break '''
    if letter_input.upper() != "Q":
        print("Sorry you are wrong, try again")
        letter_input = str(input("Guess a letter: "))
    else:
        break
print("Good work.  You are done")


for i in range (1,51):
    if i % 3 == 0:
        continue
    else:
        print(i)


from random import randint
print (randint(1,6))
