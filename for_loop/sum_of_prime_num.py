def primefector(n):
    a = []
    total = 0
    while n % 2 == 0:
        print(2)
        a.append(2)
        n = n / 2

    for i in range(3, n, 2):
        while n % i == 0:
            print(i)
            a.append(i)
            # a.
            n = n / i
    # return a
    total = sum(a)
    min(a)
    return


print(primefector(105))
