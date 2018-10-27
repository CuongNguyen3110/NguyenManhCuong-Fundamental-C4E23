items = ["game", "book", "food"]
i = int(input("Index: "))
new_value = input("New value: ")
items[i]= new_value
print(items)

items.pop(1)
print(items)

items.remove("food")
print(items)