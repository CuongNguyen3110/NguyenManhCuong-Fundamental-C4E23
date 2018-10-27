items = ["death note", "netflix", "teaching"]
print("Here is your favorite things: ", *items)

i = int(input("Position you want to update: "))
new_value = input("What thing: ")
items[i-1] = new_value
print(*items, sep = ", ")