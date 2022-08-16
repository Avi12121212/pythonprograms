def doSUm(*args):
    total = 0
    for x in args:
        total += x
    return total


a = 9
b = 6
c = sum([a, b])
# print(c)
c = doSUm(5, 4, 8, 7, 9, 12, 45, 78, 36)
# print(c)


