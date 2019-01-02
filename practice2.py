
def add_underscore(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] + "_"
    return new_word

phrase = "hello "
print(add_underscore(phrase))


''' This works '''
def check_factors(inp_num):
    for div in range(1,inp_num + 1):
        if inp_num % div == 0:
            print(f"{div} is a divisor of {inp_num}")
    return

''' Now try to do it with user input '''
def check_factors(inp_num):
    for div in range(1,inp_num + 1):
        if inp_num % div == 0:
            print(f"{div} is a divisor of {inp_num}")
    return

''' Practice the assignment on pp80 '''

def check_factors(inp_num):
    for div in range(1,inp_num + 1):
        if inp_num % div == 0:
            print(f"{div} is a divisor of {inp_num}")
    return

inp_num = float( input("Enter a number to check fators for: ") )
check_factors(inp_num)
