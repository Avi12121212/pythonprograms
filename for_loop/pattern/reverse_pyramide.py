row= 5
# for i in range(row,0,-1):
#     for j in range(row-i):
#         print("*",end=" ")
#     print(" ")

for i in range(row, 1, -1):
    for space in range(0, row-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()