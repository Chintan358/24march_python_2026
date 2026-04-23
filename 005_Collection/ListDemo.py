# l = [10,20,30,40,50,50,"abc",False,45.66]
# l = list((10,20,30,40,50))
# print(l)
# print(type(l))
# print(l[0])
# print(len(l))


#access list item :
# l = [10,20,30,40,50,60]
# print(l[1])
# print(l[1:5])
# print(l[-1])
# print(l[-4:-1])
# print(l[::-1])

#change list

# l = [10,20,30,40,50,60]

# l[0] = 100
# l.insert(3,300)
# l.append(300)
# l[:5] = [45,46,78,98,98,74,85,41]
# print(l)

# a  = [10,20,30]
# b = [40,50,60]

# a.extend(b)
# print(a)



# remove


# l = [10,20,30,40,50,60]
# l.remove(2)
# l.pop(2)

# l.clear()
# del l
# print(l)


# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1




# s = ["python","java","php","android","react"]
# l = []
# for i in s:
#     if "a" in i:
#         l.append(i)
# print(l)

# l = [i for i in s if "a" in i]
# print(l)

# k = [i for i in s if i.startswith('p')]
# print(k)



s = ["python","java","php","android","react"]
# s.sort()
# s.sort(reverse=True)
# s.reverse()

# k = sorted(s)
# print(k)

# k = s
# k = s.copy()
# k = list(s)
# k = s[:]

# k.append(5000)
# print(k)
# print(s)


l = [10,20,30,40,50,10,10]

# print(l.count(10))
# print(max(l))
# print(min(l))
# print(l.index(10))

# for i in range(len(l)):
#     if l[i] == 10:
#      print(i, l[i])
    
    

# l = [10,9,30,7,50,5]

# k = ["abc" for i in l if i%2!=0]

# print(k)

l = [1,2,10,20]

print(l[2][0])

