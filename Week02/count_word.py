def count_word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

sentence = input("문장을 입력하세요: ")
result = count_word_frequency(sentence)

for word, count in result.items():
    print(f"{word}: {count}번")