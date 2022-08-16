n1 = int(input('enter the number to get reverse febonaci= '))
n2 = int(input('enter the number to get reverse febonaci=  '))
print(n1)
print(n2)
i = 0
d = n1 - n2
# print(d)
# for n1 in range(0,0):
while d > 0:
    print(d, end=",")
    d = n1 - n2
    n1 = n2
    n2 = d
    # print(d)
print(d)
