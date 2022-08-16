class Person(object):  # Original Class
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __getitem__(self, item):
        if item == "name":
            return self.name

    def __str__(self):
        return "Name= {0},Age={1},Address= {2}".format(self.name, self.age, self.address)


class Employee(Person):
    def __init__(self, name, age, address, post, salary):
        Person.__init__(self, name, age, address)
        self.post = post
        self.salary = salary

    def __str__(self):
        return "{0},Salary={1},post={2}".format(Person.__str__(self), self.salary, self.post)


class Manager:
    def __init__(self, name, age, address, post, salary, department, secretary):
        Employee.__init__(self, name, age, address, post, salary)
        self.department = department
        self.secretary = secretary

    def __str__(self):
        return "{0},Department={1},Secretary= ({2})".format(Employee.__str__(self), self.department, self.secretary)


#
m1 = Manager("ram", 12, "Ramnagar", "senior manager", 1000, "Sales", Employee("Kohli", 90, "Delhi", "Secretary", 100))
print(m1)
# print(m1.salary)
# print(m1.post)
# print(m1.age)
# print(m1.address)
# # m1 = Person(age=24, name="Shubham", address="Peeli Kothi")
# print(m1)
e1 = Employee("sita",20,"sitapur",post="saller",salary=3000)
print(e1)
