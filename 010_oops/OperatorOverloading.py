
class Calc:

    def __init__(self,a,b):
        self.a = a
        self.b  =b

    def __add__(self, other):
        return self.a+other.a,self.b+other.b
    
    def __mul__(self, other):
        return self.a*other.a,self.b*other.b

c =  Calc(10,20)
c1 = Calc(30,40)
# k = c+c1
k= c*c1
print(k)