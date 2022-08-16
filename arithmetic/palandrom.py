max = int(input(" Please Enter the Maximum Value : "))

for num in range(1, max + 1):
    temp = num
    reverse = 0

    while (temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder**3
        temp = temp // 10
    if (num == reverse):
        print(num, end=' ')
