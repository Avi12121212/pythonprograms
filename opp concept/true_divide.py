class Data:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __truediv__(self, other):
        c1 = self.a / self.b
        c2 = other.a / other.b
        c = Data(c1, c2)
        return c

    def __gt__(self, other):
        return self.a + self.b > other.a + other.b

    def __str__(self):
        return "a= {0},b= {1} ".format(self.a, self.b)


a = Data(6, 2)
b = Data(6, 3)
c = a / b
print(c)

if a > b:
    print("big a")
else:
    print("big b")
