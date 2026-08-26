'''num = int(input("Enter the number: "))

if(num == 0):
    print("It's a Zero.")

elif(num>100):
    print("Greater than 100.")

elif(num-num is 0):
    print("Positive")'''

num = input("enter the number: ")

if(num == "0"):
    print("Its zero")

elif(num.startswith("-")):
    print("It's a Negative")

elif(num+num == num*2):
    print("positive")

elif(num>100):
    print("Greater than 100.")
    
else:
    print("Not a number")