str = [ "where", "arelklklk", "you"]
max_word = str[0]
print(len(max_word))
print(len(str))
for i in range(0,len(str)):
    if len(max_word)< len(str[i]):
        max_word= str[i]
print(max_word)