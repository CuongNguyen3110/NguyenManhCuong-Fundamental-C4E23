h = float(input("Nhap chieu cao: "))
w = float(input("Nhap can nang: "))

h1 = h / 100
bmi = w / (h1 * h1)
print(bmi)

if bmi < 16:
    print("Severly underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")