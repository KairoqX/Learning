import random

numu = int(input("Enter a number from 0 to 9: "))

numc = int(random.randint(0,9))

if numu == numc:
    print(f"You are correct the number is {numc}")
else:
    print(f"Wrong the correct number is {numc}")
    