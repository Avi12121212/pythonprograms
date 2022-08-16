class Person:  # Original Class
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return "Name= {0},Age={1},Address= {2}".format(self.name, self.age, self.address)


class Employee(Person):  # Inherited Class
    def __init__(self, name, age, address, post, salary):  # Constructor
        Person.__init__(self, name, age, address)  # Calling the super class constructor
        self.post = post
        self.salary = salary

    def __str__(self):
        return "({0}),Salary={1},Post= {2}".format(Person.__str__(self), self.salary,
                                                   self.post)  # Str using super class


p = Person("rohit", '15', 'pandeypur')
p1 = Person("rajesh", '15', 'pandeypur')
e = Employee("Popat Lal", 40, "Mumbai", "Batsman", 1000)

# p= Person()
print(p)
print(p1)
print(e)
