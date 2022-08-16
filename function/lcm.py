"""
3,7
7
14
21

24,12
"""


def lcm(n1, n2):
    max = n1 if n1 > n2 else n2
    value = max
    while value % n1 != 0 or value % n2 != 0:
        value += max
    return value

result= lcm(5,lcm(6,4))

print(result)

def addManyNumbers(*args):
    total = 0
    print(type(args))
    for x in args:
        total += x
    return total


result = addManyNumbers()
print(result)
