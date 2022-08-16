class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        add1 = self.m1 + self.m2
        add2 = other.m1 + other.m2
        s3 = Student(add1, add2)
        return s3

    def __str__(self):
        return "(M1={0}, M2={1})".format(self.m1, self.m2)

    def __gt__(self, other):
        return self.m1 + self.m2 > other.m1 + other.m2

    def __pow__(self, power):
        pow1 = self.m1 ** power
        pow2 = self.m2 ** power
        s4 = Student(pow1, pow2)
        return s4


s1 = Student(1, 2)
s2 = Student(3, 4)

s3 = s1 + s2
print(s1, s2, s3)

if s1 > s2:
    print(s1)
else:
    print(s2)

s4 = s1 ** 3
print(s1, s4)
