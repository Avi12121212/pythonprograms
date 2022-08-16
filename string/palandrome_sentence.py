def Palindrome_sentence(sentence):
    r = sentence
    r1 = r[::-1]
    r1 = r1.split()
    r = r.split()
    p = len(r)
    print(r)
    print(r1)

    for i in range(p):
        for j in range(p):
            if r[i] == r1[j]:
                print('Palindrome words are = ', r[i])

print(Palindrome_sentence("nitin sir and madam are malayalam and they are dad n mom of jalaj"))
