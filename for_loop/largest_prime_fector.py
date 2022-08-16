def isPrime(n):
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True

def maxPrimeFactor(n):
    limit = int(n ** .5)
    for i in range(limit, 1, -1):
        if n % i == 0 and isPrime(i):
            return i
    return None

n = maxPrimeFactor(100)
print(n)
