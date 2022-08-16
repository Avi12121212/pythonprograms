import book as bk

class Reader:
    def __init__(self, name, author, price):
        self.price = price
        self.name = name
        self.author = author

    def __str__(self):
        return "Name={0}, Author={1}, price= {2}".format(self.name, self.author, self.price)


b = bk.Book("Basic C", "Harsh", 200)
# r = Reader("math", "rohit", 400)
r = Reader("math", b,100)
print(r)
print(b)
