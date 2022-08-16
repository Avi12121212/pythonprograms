class StudentMarks:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other,):
        add1 = self.m1 + self.m2
        add2 = other.m1 + other.m2
        # add3 = other1.m1 + other1.m2
        add4 = add1 + add2
        s3 = StudentMarks(add1, add2)
        return s3

    def __str__(self):
        return "M1={0},M2={1}".format(self.m1, self.m2)


s1 = StudentMarks(1, 2)
s2 = StudentMarks(3, 4)
s4 = StudentMarks(3, 5)
s3 = s1 + s2
print (s3,s1)

# print(s1, s2, s4)
