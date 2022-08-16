def isPanagram(sentence):
    freq = [0 for x in range(26)]
    # print(freq)
    for ch in sentence:
        if ord(ch) < ord('a') or ord(ch) > ord('z'):
            continue
        index = ord(ch) - ord('a')
        freq[index] += 1
    # print(freq)
    for i in freq:
        if i < 1:
            return False
    return True


sentence = "A quick brown fox jumps over the lazy dog".lower()
print(isPanagram(sentence))
