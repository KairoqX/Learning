import random

name = input("Enter you name: ")
surname = input("Enter your surname: ")

p = input('''Choose you Providers:
            enter 1 for Gmail
            enter 2 for Outlook
            enter 3 for Proton
            enter 4 for Yahoo

        >>> ''')

providers = ["gmail.com","outlook.com", "proton.me", "yahoo.com"]

username = name+surname

num1 = str(random.randint(0,9))
num2 = str(random.randint(0,9))
num3 = str(random.randint(0,9))

number = num1+num2+num3


# print(number)

if p == "1":
    provider = providers[0]

elif p == "2":
    provider = providers[1]

elif p == "3":
    provider = providers[2]

elif p == "4":
    provider = providers[3]

else:
    print("Please enter valid no.")

email = username+number+provider

