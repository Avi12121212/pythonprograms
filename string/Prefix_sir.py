str = "and andorra andaman answer"
# str = "apple all"
words = str.split()
# print(words)
smallest = words[0]
n = len(smallest)
for word in words:
    # print(word)
    if len(word) < n:
        smallest = word
        n = len(smallest)
print(smallest)

while True:
    isprefix = True
    for word in words:
        if not word.startswith(smallest):
            isprefix = False
            break
    if isprefix:
        print("Prefix = ", smallest)
        break
    else:
        smallest = smallest[:len(smallest) - 1]
