
num = int(input("enter the number: "))

if(num == 0):
    print("It's a Zero.")

elif(num>100):
    print("Greater than 100.")

elif(str(num).startswith("-")):
    print("It's a Negative.")

elif(num+num == num*2) and (num%2 == 0):
    print("It's a Positive and Even number.")

elif(num+num == num*2) and (num%2 != 0):
    print("It's a Positive and Odd number.")
    
else:
    print("Not a number.")