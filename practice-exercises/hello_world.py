print("Hello, World")

'''
This line displays "Hello, World"
'''
# This line displays "Hello, World"
phrase = "hello, world"
print(phrase)

normal_string = 'normal string'
really_long_string = ''' THis is a
really long string that
spans multiple lines.  It uses triple quotes '''

print(normal_string)
print(really_long_string)

really_long_string = ''' THis is a \
really long string that \
spans multiple lines.  It uses triple quotes '''
print(really_long_string)

string1 = "abra"
string2 = "cadabra"
print(string1 + string2)
print(string1, string2)

#print the third character
#N.b. the first character is labeled 0
print(string1[2])
#print the first character
#N.b. the first character is labeled 0
print(string1[0])

#printing multiple characters
#N.b. this does NOT include the final indexed character
print(string2[1:4])

#Check length of this string
print(len(string2[1:4]))

user_input = input("Hey, what's up? ")
print("You said: ", user_input)


user_input = input("Hey, what's up? ")
user_input = user_input.upper()
print("You said: ", user_input)

input_question = input("Write something for me: ")
print(input_question)

'''Strings and numbers'''
number1 = str(15)
print(number1)
print(type(number1))
number1 = int(number1)
print(type(number1))
number2 = number1 * 5
print(number2)

print(f"{number1} multiplied by 5 is {number2}")

weight = float(0.2)
animal = str("newt")
print(f"{weight} is the weight of a {animal}")
print("{} is the weight of a {}".format(weight, animal))
print("{0} is the weight of a {1}".format(weight, animal))
print("{1} is the weight of a {0}".format(weight, animal))

'''Create your own functions'''

