value = [35, 36, 40, 44]
counter = 0
print("Answer the following algebra question: ")
print("if x = 8, then what is the value of 4(x + 3) ?")

for index, number in enumerate(value):
    print(index + 1, number, sep = ". ")

n = int(input("Your choice: "))
if n == 4 or n == 44:
    print("Bingo")
    counter += 1
else:
    print("Not correct")
print("-------------------------------------")

mean = ["About 55", "About 65", "About 75", "About 85"]
print("Estimate this answer (exact calculation not need): ")
print("Jack scored this marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?")

for index, number in enumerate(mean):
    print(index + 1, number, sep = ". ")

n = int(input("Your choice: "))
if n == 2 or n == 65:
    print("Bingo")
    counter += 1
else:
    print("Not correct")

print("You correctly answer", counter,"out of 2 questions")