# person = {
#     "name":"yash",
#     "email":"yash@gmail.com",
#     "age":22,
#     "lang":["gujarati","english","hindi"],
#     123 : "abc",
#     True : "ddss",
#     (10,20,30) : "dfd",
#     [10,20,30] : "ddsds"

# }

# print(person)


# d = dict(name="abc",email="abc@gmail.com")
# print(d)

# cn = {
#     "india":"IN",
#     "USA":"US",
#     "Canada":"CN",
#     "Australia":"AUS"
# }

# print(cn)
# print(cn.get("india1"))
# print(cn['india1'])
# print("Hello")


# print(cn.keys())
# print(cn.values())
# print(cn.items())
# print(cn)

# for i,j in cn.items():
#     print(i,j)


# cn['india']="abc"
# cn.update({"abc":"xyz","india":"K"})
# print(cn)

# cn.pop("india")
# cn.popitem()
# cn.clear()
# del cn
# print(cn)

# k = cn.copy()
# k=cn
# k.update({"A":"X"})
# print(k)
# print(cn)


student ={
    "name":"uday",
    "email":"uday@gmail.com",
    "marks" : {
        "python":20,
        "java":30,
        "php":40
    }
}

# for i,j in student['marks'].items():
#     print(i,j)


# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)

# print(thisdict)


# x = ("k1","k2","k3")
# y = (10,20,30,40)

# d = zip(x,y)
# print(list(d))

k = {"a":1,"b":2}


k.setdefault("b",3)
# k['b']=3
print(k)