name = input("Enter Student's name: ")
eng = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
mm = int(input("Enter MaxMarks per subject: "))

total = eng+maths+science
mm3 = mm*3
percentage = total/mm3*100
grade = ""
result = "Pass"
message = ""

def result_total():
    global grade, result, message
    if percentage >= 90:
        grade = "A+"
        message = "Excellent!"
    elif 90 > percentage>=80:
        grade = "A"
        message = "Good!"
    elif 80> percentage >=60:
        grade = "B"
        message = "Goood!"
    elif 60 > percentage >=50:
        grade = "C"
        message = "Needs improvement!"
    elif 50 > percentage >=40:
        grade = "D"
        message = "Needs improvement!"
    elif 40 > percentage >= 27:
        grade = "E"
        message = "Needs improvement!"
    elif percentage < 27:
        grade = "F"
        result = "Fail"
        message = "Failed!"

result_total()
print(f'''
Name: {name}
Total: {total}
Percentage: {percentage}%
Grade: {grade}
Result: {result}
**{message}**
''')