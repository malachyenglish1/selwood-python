#append - adds an item to a list
#extend
#remove - obvious
#sort - obvious

#start list with x = [], then extend
#i.e. do x = []
#then x.extend[y]

#copy list with x = y[:]


#can to lists in lists: x = [[1,2], [w,5]]
#referencing this:  x[1][0] would give us w

#creating a list from a string:
# >>> groceries = "eggs, spam, pop rocks, cheese"
# >>> grocery_list = groceries.split(", ")
# >>> print(grocery_list)
# ['eggs', 'spam', 'pop rocks', 'cheese']

desserts = ["ice cream", "cookies"]
desserts.sort()
print(desserts)

print(desserts.index("ice cream"))

food = desserts[:]
print(food)
food.extend(["brocolli", "turnips"])
print(food)

print(food)
print(desserts)

food.remove("cookies")

print(food[0:2])
