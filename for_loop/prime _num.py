num = int(input("enter the number = "))
# limit = int(num ** .5)
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("number is not prime")
            break
    else:
        print("number is prime ")
        print("number is prime ", num)
        # break
else:
    print(" number is less then 1")
