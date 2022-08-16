# a= min (2,6,7)
# print(a)


def hcf(n1, n2):
    if n1 < n2:
        min = n1
    else:
        min = n2
    while n1 % min != 0 or n2 % min != 0:
        min = min - 1



    return min


a = hcf(64, 24)
print(a)
