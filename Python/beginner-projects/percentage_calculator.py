maths = int(input("Maths marks: "))
cs = int(input("CS marks: "))
science = int(input("Science marks: "))

mm =int(input("Max marks: "))
mm3 =mm*3
total_marks = maths + cs + science

percentage = int(total_marks/mm3*100)

print(f"You got {percentage}%")