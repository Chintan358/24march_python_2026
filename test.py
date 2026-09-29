def uppercase(a):
    return a.upper()

def lowercase(a):
    return a.lower()

def greet(func,name):
    return func(name)

print(greet(lowercase,"Yash"))