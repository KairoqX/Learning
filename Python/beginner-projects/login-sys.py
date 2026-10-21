password = "12345678"
username = "KairoqX"

in_usrname = input("Enter your username: ")
in_pass = input("Enter Password: ")

if in_usrname != username:
    print("Username not found..")

elif in_pass == password:
    print("You have logged in..")
elif in_pass != password:
    print("Incorrect Password..")