# ZyLabs 11.22
# Benjamin Ojode
# 1663352

words = input("")
wordlist = words.split()

wordsFrequency = {}

for i in range(0, len(wordlist)):
    word = wordlist[i]
    if word not in wordsFrequency:
        wordsFrequency[word] = 1
    else:
        wordsFrequency[word] = wordsFrequency[word] + 1

for i in range(0, len(wordlist)):
    print(wordlist[i], wordsFrequency[wordlist[i]])