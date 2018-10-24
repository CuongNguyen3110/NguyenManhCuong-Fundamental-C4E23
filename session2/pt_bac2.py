a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

delta = b**2 - 4 * a * c
print(delta)

if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co mot nghiem:", -b/(2*a))
else:
    print("Phuong trinh co hai nghiem phan biet:")
    print("x1 =", (-b + delta ** 1/2)/(2 * a))
    print("x2 =", (-b - delta ** 1/2)/(2 * a))