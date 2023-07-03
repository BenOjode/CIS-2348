# Zylabs 8.10
# Benjamin Ojode
# 1663352

# Input word to be de-spaced and reversed
word = str(input())

# Remove spaces in the word and creates a reversed word variable
no_space_word = word.replace(' ', '')
one_word = no_space_word[::-1]

# Evaluate if the word is the same reversed or not, prints the appropriate response
if no_space_word == one_word:
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))
