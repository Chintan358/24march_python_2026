class Pen:
    price=10
    color="RED"
    company="CELLO"

    def to_write(self):
        print(self.price,self.color,self.company)

p1 = Pen()
p1.price=50
p1.to_write()

p2 = Pen()
p2.price=500
p2.to_write()