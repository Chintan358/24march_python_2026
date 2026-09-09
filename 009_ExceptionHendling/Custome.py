
class AgeInvalidException(Exception):
    pass

def check_age(a):
    if a>18:
        print("Valid age")
    else:
        raise AgeInvalidException(f"Invalid age - wait for more {18-a} years")
        

print("started")
try :
    check_age(10)
except AgeInvalidException as e:
    print(e)
print("ended")


