import random

name = input("Name: ").lower()
surname = input("Surname (enter to skip): ").lower()
provid = input('''chose provider:
0 for gmail
1 for proton
2 for outlook
3 for yahoo
>> ''')

# print(provid)
text = name+surname
provider = ["gamil.com","proton.me","outlook.com","yahoo.com"]

num1 = str(random.randint(0,9))
num2 = str(random.randint(0,9))
num3 = str(random.randint(0,9))
num = num1+num2+num3

if provid == "0":
    providers = provider[0]
elif provid == "1":
    providers = provider[1]
elif provid == "2":
    providers = provider[2]
elif provid == "3":
    providers = provider[3]
else:
    print("Please enter a valid provider id")
print("Your email is",text+num+"@"+providers)
