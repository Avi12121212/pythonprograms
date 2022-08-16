lower = int(input("enter the number of lower range  = "))
upper = int(input("enter the number of upper range  = "))
count= 0
for num in range(lower, upper + 1):

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # print("i= ", i)
                # print("number is not prime")
                break
        else:
            # print("number is prime ")
            print(num)
            count = count + 1


    else:
        print(" number is less then 1")
print(count)