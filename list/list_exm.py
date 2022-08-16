l1 = [1, 2, 3, 4]
print(l1)

add = 0
for i in range(0, 4):
    add = add + l1[i]
    print(l1[i])
print(add)

for i in l1:
    add = add + i
    print(i)
print(add)

n = len(l1)
print("size=", n)

a = [i + 1 for i in range(0,4)]
print('a= ',a)
# for i in range(n):
# print(i, "=", l1[i], end=",")
# print()
# l1[1] = 100
# for i in range(n):
#     l1[i]+=1
# for i in range(n):
#     print(i, "=", l1[i], end=",")
# # q= []
# # print((type(q)))
# # fruit= ['apple','banana','orange']
# # l= [1,3,4,6]
# # print(fruit.index('orange'))
# # p= fruit+ l
# # print(p)
#
#
# # l1 = [100, 10, 2, 5]
# # # [i + 1 for i in l1]
# # for i in range(0,4):
# #     # print(l1[i] +1)
# print()
# a=[x for x in range(1,11)]
# print(a)
# a=[x*x for x in range(1,11)]
# print(a)
# a=[x-1 for x in a]
# print(a)
