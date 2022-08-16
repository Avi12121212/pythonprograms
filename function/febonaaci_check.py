
def checkForFib(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    a = 0
    b = 1
    c = a + b
    while c < n:
        a = b
        b = c
        c = a + b
    if c == n:
        return True
    else:
        return False


for i in 8:
    if checkForFib(i):
        print(i, end=",")


