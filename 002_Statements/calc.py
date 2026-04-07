
cont = 'y'
while cont !='n':
    a = int(input("enter number : "))
    b = int(input("enter number : "))
    choice = input("enter choice : +,-,*,/ : ")
    match(choice):
        case "+":
            print(f"addtion of {a} and {b} is {a+b}")
        case "-":
            print(f"substration of {a} and {b} is {a-b}")
        case "*":
            print(f"multiplication of {a} and {b} is {a*b}")
        case "/":
            print(f"devison of {a} and {b} is {a/b}")
        case _ :
            print("Invalid choice")

    cont = input("Do you want to contineu ? y or n ? :")



