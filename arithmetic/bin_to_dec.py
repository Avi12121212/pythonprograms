bin = int(input('enter the the binary =  '))
decimal = 0
m = 1
while bin > 0:
    r = bin % 10
    bin = bin // 10
    decimal = decimal + m * r
    m = m * 2
print(decimal)


