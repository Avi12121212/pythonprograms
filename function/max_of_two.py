def maxi(a, b, c):
    if a > b & a > c:
        max = a
    if b > a & b > c:
        max = b
    else:
        max = c
    return max

# p= maxi(2,5,7)
print(maxi(1, 2, 3))
