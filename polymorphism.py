a = "1"
b = "2"
total = a + b
print(total)
a = 1
b = 2
total = a + b
print(total)


def add(a=0, b=0):
    print("a=", a, ", b=", b)
    return a + b


print(add())
print(add(1))
print(add(1, 2))
print(add(b=9))

class A:
    def f(self):
        print("F in A")
class B:
    def f(self):
        print("F in B")
a=A()
b=B()
a.f()
b.f()
