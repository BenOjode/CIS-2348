# ZyLabs 9.10
# Benjamin Ojode
# 1663352

import csv

# Open the input file and separate the content of the file into individual lines
file_name = input()
new_file = open(file_name)
file_content = csv.reader(new_file, delimiter=',')
lines = []
for row in file_content:
    for word in row:
        lines.append(word.strip())

# Search for words in the file, numerating their frequency, outputting without any duplicates
for i in range(len(lines)):
    if lines[i] not in lines[:i]:
        count = 0
        for word in lines:
            if lines[i] == word:
                count += 1
        print(lines[i], count)
new_file.close()
