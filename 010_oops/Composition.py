class Salary : 
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salay(self):
        return (self.pay*12)+self.bonus
    
class Employee:

    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age  =age
        self.salary = Salary(pay,bonus)

    def total_salary(self):
        return self.salary.annual_salay()
    

e  = Employee("Raj",22,5000,2000)
print(e.total_salary())