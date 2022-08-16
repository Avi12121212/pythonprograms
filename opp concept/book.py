class Book:
    def __init__(self, b_name, b_author, b_price):
        self.b_name = b_name
        self.b_author = b_author
        self.b_price = b_price

    def __str__(self):
        return "Book name  = {0},Book author= {1},book price= {2}".format(self.b_name, self.b_author, self.b_price)

"""
b1 = Book("math", "ravi", 200)
b2 = Book("english", "rajesh", 5000)
print(b1)
print(b2)
"""
