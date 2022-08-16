bin = int(input('enter the the binary =  '))
octa_decimal = 0
m = 8
while bin > 0:
    r = bin % 10
    bin = bin // 10

    octa_decimal = octa_decimal + m * r
    m = m ** 2
print(octa_decimal)


