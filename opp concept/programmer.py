class Programmer:
    def __init__(self, name ,product):
        self.name= name
        self.product= product
    def __str__(self):
        return"Programmer= {0}, Product= {1}".format(self.name, self.product)

p1= Programmer("rohit", "skype")
print(p1)