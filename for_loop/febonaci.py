# print the Fibonacci Sequence
n =int(input('enter the turms to add= '))
a= 0
b=1
i=0
print(a,b)
for i in range(2,n):
    c= a+b
    a=b
    b=c
    print(c)
