class Student:

    clg = "XYZ"
    def __init__(self,name,email,age):
        self.name = name
        self.email =email
        self.age = age

    def display(self):
        print(self.name,self.email,self.age,self.clg)

    @classmethod
    def test(cls):
        print(cls.clg)

    @staticmethod
    def demo():
        print("static calling")
        


Student.clg="ABC"

s = Student("sahil","sahil@gmail.com",24)
s.display()

s1 = Student("Kenil","kenil@gmail.com",22)
s1.display()

Student.test()
Student.demo()