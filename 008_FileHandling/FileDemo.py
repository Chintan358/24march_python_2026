# f = open("test.txt",'w')
# # f.write("something")
# f.writelines(["Hello\n","python\n","Hello\n","Java"])
# f.close()

# f = open("test.txt",'a')
# # f.write("something")
# f.writelines(["Hello\n","Tops\n","Hello\n","surat"])
# f.close()

# f = open("test.txt",'r')
# # data = f.read()
# data  =f.readlines()
# print(data)
# f.close()


# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if 'e' in data:
#         print(data)
#     if not data :
#         break

# with open("home.txt",'w') as f:
#     f.write("Write something..")


# with open("home.txt",'r') as f:
#     print(f.tell())
#     f.seek(5)
#     data = f.read()
#     print(f.tell())
#     print(data)


# with open("abc.txt",'a+') as f:
#     f.write("Write something")
#     f.seek(0)
#     data = f.read()
#     print(data)


# with open("abc.jpg",'rb') as f:
#     data = f.read()
#     print(data)

import json
# d = {"name":"yash","email":"yash@gmail.com"}
# with open("data.json",'w') as f:
#     json.dump(d,f)



with open("data.json",'r') as f:
    data = json.load(f)
    print(data)

