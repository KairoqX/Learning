import random

number_user = int(input("Enter your number between 0 to 9: "))

number_computer = random.randint(0,9)

if number_user == number_computer:
    print(f"You won the number is {number_computer}")

else:
    print(f"Wront the number is {number_computer}")