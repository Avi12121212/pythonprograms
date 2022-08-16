def reverse_sentence(sentence):
    po = sentence.split()
    print(po)
    l1 = po[::-1]

    print(l1)
    reversed_sentence = ' '.join(l1)
    print(reversed_sentence)

    reversed_sentence = ' '.join(reversed(po))
    return (reversed_sentence)


print(reverse_sentence("o god you are amazing"))
