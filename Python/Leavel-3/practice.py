name = input("enter name: ")
print(f"Good Afternoon {name}")

date = input("date: ")
letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
'''

print(letter.replace("<|Name|>", "name").replace("<|Date|>", "date"))

name ="Mahiru is a cute  girl"

print(name.find("  "))

print(name.replace("  "," "))

letter2 = '''
        Dear <|Name|>,\n\tYou are selected\n <|Date|>
'''

print(letter2)