items = ["T-shirt", "Sweater"]
n = input("Welcome to our shop, what do you want ( C, R, U, D )? ").upper()

while n != "C" and n != "R" and n != "U" and n != "D":
    print("Not ok")
    n = input("Welcome to our shop, what do you want ( C, R, U, D )? ")

if n == "R":
    print("Our items: ", *items, sep = ", ")
if n == "C":
    new_items = input("Enter new items ? ")
    items.append(new_items)
    print("Our items: ", *items, sep = ", ")
if n == "U":
    i = int(input("Update position ? "))
    while i-1 > len(items):
        print("index out of range")
        i = int(input("Update position ? "))
    new_value = input("New item ? ")
    items[i-1] = new_value
    print("Our items: ", *items, sep = ", ")
if n == "D":
    i = int(input("Delete position ? "))
    while i-1 > len(items):
        print("index out of range")
        i = int(input("Delete position ?"))
    items.pop(i-1)
    print("Our items: ", *items, sep = ", ")


























