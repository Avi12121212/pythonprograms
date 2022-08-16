class Calculater:
    def __init__(self, num):
        self.number = num

    def square(self):
        return "Square of number= {0}".format(self.number **2)
    def root(self):
        return "square root of number= {0}".format(self.number**.5)

a = Calculater(9)
print(a.square())
print(a.root())


print(a)