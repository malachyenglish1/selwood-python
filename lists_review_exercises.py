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
