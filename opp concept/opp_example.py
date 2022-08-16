"""
Make software components and combine them
How do you design a car?
1. You decide the final features of the class
2. Break this into parts
3. Break parts into sub-parts till individual parts become very simple
4. Make the parts and combine
5. Car is ready
This is top-down design
The next car will be made using the already manufactured components. This is
bottom up design.

Some parts will be redesigned.

OOPS terms
1. Class - the paper design of the Car
2. Object- the actual car
3. Encapsulation- Aggregation of objects with the interfaces showing
4. Abstraction- Keep in a blackbox with only the command showing
5. Polymorphism- The same command taking different meanings at different times
6. Inheritance- Development with backward compatibility.
7. Modularity- Parts of the software that can be developed separately.
Separate editing, separately compiled, test separately and combine.
8. Add to the car body.- Constructor


"""


class Student:
    def __init__(self, name, rollno, classno):  # Constructor. It is called when the object is constructed
        self.name = name
        self.rollno = rollno
        self.classno = classno

    def __str__(self):  # String representation of the class
        return "Roll No={0}, Name={1}, Class = {2}".format(self.rollno, self.name, self.classno)


s1 = Student("Sachin", "10", 5)  # Calling the constructor
s2 = Student("Sourav", "10", 5)  # Calling the constructor
print(s1,s2)  # Prints output of the __str__ function
