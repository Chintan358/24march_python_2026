# a = [1,2,3,4,5,6,7,8,9]
# k = []

# def checkodd(a):
#     if a%2!=0:
#         return a
    
# for i in a:
#     j = checkodd(i)
#     if j is not None:
#         k.append(j)

# print(k)



# a = [1,2,3,4,5,6,7,8,9]
# def checkodd(a):
#     if a%2!=0:
#         return a 
# k = filter(checkodd,a)
# print(list(k))


# a = [1,2,3,4,5,6,7,8,9]
# k = filter(lambda i:i%2!=0,a)
# print(list(k))

sub = ["java","python","node","php","android"]

# k = filter(lambda ele : "a" in ele,sub)
k = filter(lambda ele : ele.startswith("p"),sub)
print(list(k))