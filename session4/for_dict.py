p1 = {
    "name": "H.Duc",
    "age": 23,
    "city": "Hai Phong"
}

p2 = {
    "name": "Quan",
    "age": 24,
    "city": "Hanoi"
}
p_list = [
    {
        "name": "H.Duc",
        "age": 23,
        "city": "Hai Phong"
    },
    {
        "name": "Quan",
        "age": 24,
        "city": "Hanoi"
    }   
]

print(p_list)
for p in p_list:
    print(p["age"])
    print("---------")

# for k in person.keys(): # tuple ~ list
#     print(k, person[k])

# for v in person.values():
#     print(v)

# for k, v in person.items():
#     print(k, v)

    