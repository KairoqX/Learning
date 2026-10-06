
while True:
    x,y,z = input("Enter The expression: ").split(" ")
    x1 =int(x)
    z1 =int(z)

    if(x1==0)and(y=="/"):
        print(0)
    elif(z1==0)and(y=="/"):
        print(0)
    elif(y=="+"):
        print(x1+z1)
    elif(y=="-"):
        print(x1-z1)
    elif(y=="*"):
        print(x1*z1)
    elif(y=="/"):
        print(x1/z1)
    else:
        print("invalide")
        break