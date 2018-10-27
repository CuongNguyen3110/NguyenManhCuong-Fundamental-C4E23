items = ["death note", "netflix", "teaching"]

print("Here is your favorite things: ", *items)

i = int(input("Position you want to delete: "))
items.pop(i)
print(items)