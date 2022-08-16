def isPrime(n):
    if n < 2:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


def reverseNumber(n):
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev


def isTwistedPrime(n):
    rev = reverseNumber(n)
    if isPrime(n) and isPrime(rev):
        return True
    else:
        return False


# for i in range(101):
#     if isTwistedPrime(i):
#         print(i, end=",")

print(isTwistedPrime(79))