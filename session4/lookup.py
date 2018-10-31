code = {
    "hc": "hoc",
    "eny": "em nguoi yeu",
    "lm": "lam"
}

while True:
    key = input("Your code ? ")
    if key in code:
        print(code[key])
    else:
        a = input("Not found, do you want to contribute this word? (Y/N) ? ").upper()
        while a != "Y" and a != "N":
            a = input("Not found, do you want to contribute this word? (Y/N) ? ").upper()
        if a == "Y" or a == "YES":
            translate = input("Enter your translation: ")
            code[key] = translate
        if a == "N" or a == "NO":
            print("OK")
    print(code)





