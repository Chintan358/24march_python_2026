class Pen:

    def __init__(self,price,color,company):
        self.price=price
        self.color = color
        self.company = company

    def display(self):
        print(self.price,self.color,self.company)

class NoteBook(Pen):

    def __init__(self, price, color, company,pages):
        self.pages = pages
        super().__init__(price, color, company)

    def display(self):
        print(self.price,self.color,self.company,self.pages)

p = Pen(30,"RED","cello")
p.display()

n = NoteBook(40,"White","Classmate",50)
n.display()