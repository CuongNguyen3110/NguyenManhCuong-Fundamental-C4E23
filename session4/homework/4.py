value = [35, 36, 40, 44]

print("Answer the following algebra question: ")
print("if x = 8, then what is the value of 4(x + 3) ?")

for index, number in enumerate(value):
    print(index + 1, number, sep = ". ")

n = int(input("Your choice: "))
if n == 4 or n == 44:
    print("Bingo")
else:
    print("Not correct")

