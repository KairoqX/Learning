import random

# getting the number by user
numu = int(input("Enter a number from 0 to 9: "))
# genrating number by computer
numc = int(random.randint(0,9))

# checking if the number is correct
if numu == numc:
    print(f"You are correct the number is {numc}")
else:
    print(f"Wrong the correct number is {numc}")
