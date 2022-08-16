class Person:
    def __init__(self, name, address, mobile_no):
        self.name = name
        self.address = address
        self.mobile_no = mobile_no

    def __str__(self):
        return "Name = {0}, Address= {1}, Mobile_no= {2}".format(self.name, self.address, self.mobile_no)


# class Employee(Person):
#     def __init__(self, name, address,mobile_no,post,salary):
#         Person.__init__(self,name,address,mobile_no)
#         # self.name= name
#         # self.address= address
#         # self.mobile_no= mobile_no
#         self.post= post
#         self.salary= salary

class Addressbook:
    def __init__(self, persons):
        self.persons = persons

    def search(self, name):
        for person in persons:
            if person.name.lower().startswith(name.lower()):
                print(person)

    # def __str__(self):
    #     return "{0}, Post= {1}, Salary= {2}".format(Person.__str__(self),self.post,self.salary)


person = [Person("rohit", "vns", "9936848228"), Person("avinash", "bns", "9936848228"),
          Person("golu", "bihar", "9936848228")]
print(person)
add = Addressbook(persons)
add.search("rohit")
