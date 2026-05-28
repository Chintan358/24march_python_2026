class Salary : 
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salay(self):
        return (self.pay*12)+self.bonus
    
class Employee:

    def __init__(self,name,age,s):
        self.name = name
        self.age  =age
        self.salary = s

    def total_salary(self):
        return self.salary.annual_salay()
    
s = Salary(10000,5000)
e  = Employee("Raj",22,s)
print(e.total_salary())