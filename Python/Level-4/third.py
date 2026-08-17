name = "Mahiru" #it's a string or str
surname = 'Shiina' #it's also a str
# M is 0 or -5
# a is 1 or -4
# h is 2 or -3
# r is 3 or -2
# u is 4 or -1
# strings are immutable or you can't change it you have to create a new string to change
print(len(name))
nameshort = name[0:3] # start from 0 and include 2 not 3
print(nameshort)
print(name[-5:-1])
print(name[1:])
print(name[1:5])
print(name[:5])
character1 = name[1]
print(character1)

word = "amazing"

word[1:6:2]
print(word)

print(name.endswith("iru"))
print(name.startswith("mah"))
print(name.capitalize())
print(name.lower())
print(name.upper())
s = "ram ram bhailog"
index = s.find("bhailog")
print(index)



# escape secuence
# \n new line
# \t give tab amount space 
# \"\" prints "
# \\ prints \
