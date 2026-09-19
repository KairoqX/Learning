marks = int(input("Enter your marks: "))

while True:
    if 0 > marks or marks > 100:
        print(f"How the hell you got {marks} marks? you lil lier(-_-)")
    elif marks >=90:
        print("A/Pass")
    elif 80 <= marks <= 89:
        print("B/Pass")
    elif 70 <= marks <= 79:
        print("C/Pass")
    elif 60 <= marks <= 69:
        print("D/Pass")
    else:
        print("E/Fail")
    marks = int(input("Enter your marks: "))

