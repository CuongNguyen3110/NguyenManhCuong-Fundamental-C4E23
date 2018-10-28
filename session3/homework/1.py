print("Hi there, this is a superuser gateway")
user_name = input("Username: ")

while user_name != "c4e":
    print("You are not superuser")
    user_name = input("Username: ")

password = input("Password: ")

while password != "codethechange":
    print("Password is incorrect")
    password = input("Password: ")
print("Welcome, c4e")


