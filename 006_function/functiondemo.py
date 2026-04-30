
# def message():
#     print("Hello python")

# def square(a):
#     print(f"square of {a} is {a*a}")

# def sum(a,b):
#     print(f"addtion od {a} and {b} is {a+b}")


# def cube(a):
#     q = a*a*a
#     return q


# message()
# square(10)
# sum(10,20)

# q = cube(10)
# print(q)
# print(cube(4))


# def person(name,email="abc@gmail.com",age=0):
#     print(name,email,age)

# person("raj",age=15)


# def add(*a):
#     sum = 0
#     for i in a:
#       sum+=i
#     print(sum)

# add(10,20,30)

# def person(**k):
#     print(k)

# person(name="abc",email="xyz",age=25)


add = lambda a,b:a+b
sq = lambda a : a*a

print(add(10,20))
print(sq(10))