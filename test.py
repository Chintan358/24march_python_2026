# import math

# c = 50
# h = 30
# s = "100,150,180"
# l = s.split(",")
# v = []

# for d in l:
#     k = round(math.sqrt(2*c*float(d)/h))
#     v.append(k)

# print(v)


k = input("enter length")
l = k.split(",")
row = int(l[0])
col = int(l[1])


d = [[0 for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
       d[i][j]=i*j

print(d)