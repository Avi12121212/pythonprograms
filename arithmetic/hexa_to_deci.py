hex = "A"  # input('enter the hexadecimal = ')
base = 16
dec = 0
m = 1
n = len(hex)
for i in range(n - 1, -1, -1):
    x = hex[i]
    if x >= '0' and x <= '9':
        dec += int(x) * m
        m = m * base
    else:
        orda = ord(x) - ord('A')
        orda += 10
        dec += orda * m
        m = m * base
print(dec)
