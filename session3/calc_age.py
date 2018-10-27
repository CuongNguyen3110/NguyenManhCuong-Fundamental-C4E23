yob_str = input("Year of birth? ")

while not yob_str.isdigit():
    print("Not ok")
    yob_str = input("Year of birth? ")
    
yob = int(yob_str)
age = 2018 - yob
print(age)

