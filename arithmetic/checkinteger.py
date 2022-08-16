number = int(input("enter the num= "))
r = number ** .5
print(type(number))

if int(r + 0.5) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")