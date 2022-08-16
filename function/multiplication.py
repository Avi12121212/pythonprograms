
def domulti(*args):
    total = 1
    for x in args:
        total = total * x
    return total


d = domulti(2, 3, 4)
print(d)