str = ["Andman", "Andorra","Andwp"]
minlen = len(str[0])
for i in range(1, len(str)):
    minlen = min(minlen, len(str[i]))
    print(minlen)
add = ''
for i in range(minlen):
    si = str[0][i]
    # print(si)
    for j in range(1, len(str)):
        if str[j][i] == si:
            print(si)


