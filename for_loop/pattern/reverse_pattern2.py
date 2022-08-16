num = 5
# for i in range(1, num + 1):
#     for j in range(1, num - i + 1):
#         print(" ", end=" ")
#     for j in range(i, 0, -1):
#         print("*", end=" ")
#     for j in range(2, i + 1):
#         print("*", end=" ")
#     print( )

for i in reversed( range(1, num+1 )):
    for j in range(1, num - i + 1):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print("*", end=" ")
    for j in range(2, i + 1):
        print("*", end=" ")
    print()
    # for j in range(1,0,-1):
    #     print(j,end="" )

