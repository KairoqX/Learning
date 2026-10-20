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
provider = ["gmail.com","proton.me","outlook.com","yahoo.com"]

num = ""

for i in range(4):
    a = str(random.randint(0,9))
    num+=a

if provid == "0":
    providers = provider[0]
    print("Your email is",text+num+"@"+providers)
elif provid == "1":
    providers = provider[1]
    print("Your email is",text+num+"@"+providers)
elif provid == "2":
    providers = provider[2]
    print("Your email is",text+num+"@"+providers)
elif provid == "3":
    providers = provider[3]
    print("Your email is",text+num+"@"+providers)
else:
    print("Please enter a valid provider id")



