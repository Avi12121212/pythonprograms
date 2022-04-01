a = 10
b = 11
if a > b:
    maxValue = a
else:
    maxValue = b
print(maxValue)
c = 90
if a >= b and a >= c:
    maxValue = a
elif b >= c:
    maxValue = b
else:
    maxValue = c
print(maxValue)
