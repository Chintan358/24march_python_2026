print("Progrma started")
try :
    a = 10
    b = a/0
    print(b)
except ZeroDivisionError as e:
    print(e)
else:
    print("something")
finally:
    print("always executable")
print("Program ended")