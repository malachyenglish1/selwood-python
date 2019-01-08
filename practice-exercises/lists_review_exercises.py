desserts = ["ice cream", "cookies"]
print(desserts)

print(desserts.index("ice cream"))

food = desserts[:]
print(food)

food.extend(["brocolli","turnips"])
print(food)

food.remove("cookies")
print(food)

print(food[0:2])

breakfast_comment = "cookies, cookies, cookies"
breakfast = breakfast_comment.split(", ")
print(breakfast)


def less_than_n():
    num_list = [2, 4, 8, 16, 22, 32, 64]
    print("Initial list is: ", num_list)
    print(type(num_list))
    print(type(num_list[0]))
    small_num_list = []
    for i in range(len(num_list)):
        if num_list[i] < 20:
            small_num_list.append(num_list[i]) 
    print("Final list is: ", small_num_list)
    return num_list

less_than_n()


'Assignment - list of lists
