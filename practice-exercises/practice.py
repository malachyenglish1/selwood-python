'''
base_num = input("Enter a base number: ")
base_num = float(base_num)
power_num = input("Enter an exponent: ")
power_num = float(power_num)
print(f"{base_num} raised to the power of {power_num} is ", base_num ** power_num)
'''

def cube(num1):
    print(num1 **3)
    return

def multiply(num1, num2):
    mult_result = num1 * num2
    print(f"{num1} multiplied by {num2} is", mult_result)
    return

multiply(2,5)

'''practicing loops'''
'''WHILE loop'''
n=1
while (n <= 5):
    print("n = ", n)
    n = n + 1
print("Loop finished")

'''FOR loop - N.b. we do not also process the last number'''    
for n in range(1, 5):
    print("n = ", n)
print("Loop finished")


for i in range(1,4):
    for j in ["A", "B", "C"]:
        print("i = ",i, "j = ", j)

for i in range(2,11):
    print (i)
    i = i + 1

f = 2
while (f <= 10):
    print(f)
    f = f + 1

def doubles(inp_num):
    for i in range(1,4):
        j = inp_num * (2 ** i)
        print(j)
    return

def invest(amount, rate, time):
    print(f"principal amount: $",str(amount))
    print(f"annual rate of return: ",str(rate))
    time = time + 1
    for i in range(1,time):
        print(f"year {i}: $", str(amount * ((1 + rate) ** i)))
    return

