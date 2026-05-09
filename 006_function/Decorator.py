# def after(func):
#     def execute():
#         func()
#         print("calling after test")
#     return execute


# def before(func):
#     def execute():
#         print("calling before test")
#         func()
#     return execute


# @after
# def test():
#     print("test calling")


# test()


# def add(func):
#     def execute(*a):
#         print("Addtion : ")
#         sum = 0
#         for i in a:
#             sum+=i
#         print("addtion is : ",sum)
#         func(*a)
#     return execute


# def mul(func):
#     def execute(*a):
#         print("Multiplcation : ")
#         sum = 1
#         for i in a:
#             sum*=i
#         print("mul is : ",sum)
#         func(*a)
#     return execute

# @add
# @mul
# def calc(a,b):
#     pass

# calc(10,20)


def numbersOnly(func):
    def execute(a):
        if str(a).isdigit():
            func(a)
        else:
            print("Invalid input")
    return execute

@numbersOnly
def get(a):
    print(a)

get("10sds")