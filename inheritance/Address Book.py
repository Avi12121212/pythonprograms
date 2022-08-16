class Person:
    def __init__(self, name, address, mobile_no):
        self.name = name
        self.address = address
        self.mobile_no = mobile_no

    def __str__(self):
        return "Name = {0}, Address= {1}, Mobile_no= {2}".format(self.name, self.address, self.mobile_no)


class AddressBook:
    def __init__(self, persons):
        self.persons = persons

    def search(self, name):
        for person in persons:
            if person.name.lower().startswith(name.lower()):
                print(person)


persons = [Person("Rajiv", "Bangalore", "7678657"), Person("Rajesh", "delhi", "1463254"),
           Person("Rajendra", "gurgaon", "1452541")]
add = AddressBook(persons)
add.search("raji")
