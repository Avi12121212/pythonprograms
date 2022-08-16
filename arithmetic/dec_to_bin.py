a = 59
base = 16
output = ""
while a >= 1:
    r = a % base
    if r <= 9:
        output = str(r) + output
    else:
        orda = ord('A')  # ord function gives ascii value. In this case 65
        diff = r - 10
        newchar = chr(orda + diff)  # Chr converts ascii value to character
        output = newchar + output

    a = a // base
print(output)
