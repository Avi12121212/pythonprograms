def Proper_case(sentence):
    ch = sentence.split()
    l = len(ch)
    # print(l)
    for j in range(len(ch) - 1):
        i = ch[j]

        if i == l - 1:
            print(i[l - 1])
        print(i[0].upper(), end=" ")
    print(ch[len(ch) - 1].upper())


print(Proper_case("mahendra singh dhoni"))
