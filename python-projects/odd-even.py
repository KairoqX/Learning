while True:
    num = int(input("enter the num: "))

    if(num==0):
        print("zero")

    elif(num < 0):
        print("It's a negative number..")

    elif(num > 0)and(num%2==0):
        print("It' a positive even number..")

    elif(num > 0)and(num%2!=0):
        print("It's positive odd number..")

    else:
        print("invalide")
        break