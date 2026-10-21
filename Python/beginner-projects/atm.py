balance = 0
state = False

# ATM Functions
def atm(command):
    global balance, state
    if command == 1:
        print(f"Your balance is ${balance}")

    elif command == 2:
        withdraw = int(input("Enter The amount you want to withdraw" \
        ": "))
        if withdraw > balance >= 0:
            print(f"Insufficient balance you have ${balance}")
        else:
            n = balance - withdraw
            print(f"Successful withdrawal you now have ${balance}")

    elif command == 3:
        deposit = int(input("Enter the amount you want to deposit" \
        ": "))
        balance+= deposit
        print(f"Deposit successful you balamce is ${balance}")
    else:
        state = False

    

# Login system
def login():
    password = "1234"
    username = "KairoqX"
    global state
    in_usrname = input("Enter your username: ")
    in_pass = input("Enter Password: ")

    if in_usrname != username:
        print("Username not found..")
    elif in_pass == password:
        print("You have logged in..")
        state =True
    elif in_pass != password:
        print("Incorrect Password..")


# execution      
login()
while state:
    try:
        global command
        command = int(input("PyATM(type 1 for balance, 2 for widtdraw, 3 for deposit, 4 to exit)" \
        ": "))
        atm(command)
    except ValueError:
        print("Command not found")
        atm(command)