camel = input("Camel case: ")

snake= ""

for i in camel:
    if i.islower():
        snake += i
    elif i.isupper():
        snake+= "_" + i.lower()
print(snake)
        