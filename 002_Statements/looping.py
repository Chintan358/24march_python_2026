
# for i in range(10):
#     print(i)

# for i in range(5,10):
#     print(i)


# for i in range(1,10,3):
#     print(i)

# for i in range(10,0,-2):
#     print(i)


# i = 21
# while i<20:
#     print(i)
#     i+=1


choice = "y"

while choice !="n" :
    marks = int(input("Enter marks " ))

    if marks>90 and marks<=100:
        print("Grade A")
    elif marks>70 and marks<=90:
        print("Grade B")
    elif marks>50 and marks<=70:
        print("Grade C")
    elif marks>35 and marks<=50:
        print("Grade D")
    elif marks>=0 and marks<=34:
        print("Grade F")
    else :
        print("Invalid marks")

    choice = input("do you want to continue? press y or n")
    
