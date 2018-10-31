p1 = {
    "name": "Huy",
    "Hours": 30,
    "VND per hour": 50
}
p2 = {
    "name": "Quan",
    "Hours": 20,
    "VND per hour": 40
}
p3 = {
    "name": "Duc",
    "Hours": 15,
    "VND per hour": 35
}

person = [p1, p2, p3]
print(person)

t = 0
for h in person:
    print("Gio lam cua", h["name"], h["Hours"])
    l = h["Hours"] * h["VND per hour"]
    print("Luong cua", h["name"], l)
    t = t + l
print("Tong luong", t)
