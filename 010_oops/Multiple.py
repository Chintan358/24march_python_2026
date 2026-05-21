class A:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("a cons calling")

    def display(self):
        print("A display calling")
        # print(self.x,self.y)

class B:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("b cons calling")
       

    def display(self):
        # print(self.x,self.y,self.z)
        print("B display calling")


class C(B,A):
    
    def __init__(self, x, y):
       B(x,y).__init__(x, y)


c = C(10,20)
c.display()