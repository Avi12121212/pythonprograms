def primefector(n):
    a = []
    total = 0
    minimum= 0
    while n % 2 == 0:
        print(2)
        a.append(2)
        n = n / 2

    for i in range(3, int(n), 2):
        while n % i == 0:
            print(i)
            a.append(i)
            # a.
            n = n / i
    # return a
    total = sum(a)
    len(a)
    if len(a)<3:
        print("number has atleast three prime number ")
    return len(a)

print(primefector(15))
