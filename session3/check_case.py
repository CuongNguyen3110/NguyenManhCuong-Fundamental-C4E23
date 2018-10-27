s = input("Enter a text: ")

if not s.isdigit() not s.islower() and not s.isupper():
    print("Contains both lowercase and uppercase")
else:
    print("Not Ok")