password = input("Nhap password: ")

while len(password) <= 8 \
    or password.isalpha() \
    or password.islower() or password.isupper():
    print("Not ok")
    if len(password) <= 8:
        print("Password length must be greater than 8")
    if password.isalpha():
        print("Password must contain number")
    if password.islower() or password.isupper():
        print("Password must contain both upper and lower characters")
    password = input("Nhap password: ")

   

