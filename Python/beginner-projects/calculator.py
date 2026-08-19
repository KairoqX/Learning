x = int(input("first no: "))
y = (input("+, -, *, /: "))
z = int(input("second no: "))

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x//z)
else:
    print("invalide")

