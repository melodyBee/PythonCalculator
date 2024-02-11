while True:
    a = int(input("num 1 = "))
    b = int(input("num 2 = "))
    c = input("Enter any sign +, -, *, / = ")

    if c == "+":
        result = a + b
    elif c == "-":
        result = a - b
    elif c == "*":
        result = a * b
    elif c == "/":
        result = a / b
    else:
        result = "You have entered the wrong sign."

    print(result)
    print("Do you want to continue? (yes/no)")
    cont = input()
    if cont == "no":
        break
    else:
        continue

