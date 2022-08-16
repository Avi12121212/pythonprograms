str = "biest nicest surest est"
words = str.split()
smallest = words[0]
print(smallest)
l = len(smallest)
print(l)
for word in words:
    if len(word) < l:
        smallest = word
        l = len(smallest)
print(smallest)

while True:
    is_suffix = True
    for word in words:
        if not word.endswith(smallest):
            is_suffix = False
            break
    if is_suffix:
        print("suffix=", smallest)
        break
