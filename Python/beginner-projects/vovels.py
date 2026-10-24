sentence = "Your Highness 👑, please do not be angry with this humble knight. ⚔️".lower()
vovel = ['a','e','i','o','u']

counter = 0

for i in sentence:
    for x in vovel:
        if i == x:
            counter+=1
print(f"There are {counter} vovels in this sentence.")