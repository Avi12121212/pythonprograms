max = int(input("Enter a number: "))
# sum = 0
# temp = num
for num in range(1, max + 1):
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** 3
        num //= 10

    if temp == sum:
        print(temp, "is an Armstrong number")
