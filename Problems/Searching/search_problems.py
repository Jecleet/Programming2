'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
file = open('../searching/dictionary.txt', 'r')
words = []
max_length = 0
max_length_words = []
for line in file:
    for i in split_line(line):
        words.append(i)
for word in words:
    if len(word) > max_length:
        max_length = len(word)
for word in words:
    if max_length == len(word):
        max_length_words.append(word)
print(*max_length_words)

# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
file = open('../searching/AliceInWonderLand.txt', 'r')
words = []
word_count = 0
word_length_total = 0
for line in file:
    for i in split_line(line):
        words.append(i.upper())
for word in words:
    word_count += 1
    word_length_total += len(word)
print("The word count is", word_count)
print("The average word length is", word_length_total / word_count)


# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_count = 0
for word in words:
    if word.upper() == "ALICE":
        alice_count += 1
print(alice_count)


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
seven_letter_words = []
word_length_max = 0
for word in words:
    if len(word) == 7:
        seven_letter_words.append(word.upper())

for word in seven_letter_words:
    if words.count(word) > word_length_max:
        word_length_max = words.count(word)
        max_length_word = word
print(max_length_word)

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

chesire_count = 0
for word in words:
    if word.upper() == "CHESHIRE":
        chesire_count += 1
print(chesire_count)

cat_count = 0
for word in words:
    if word.upper() == "CAT":
        cat_count += 1
print(cat_count)

chesire_cat_count = 0
word_count = 0
for word in words:
    word_count += 1
    if word.upper() == "CHESHIRE":
        if words[word_count].upper() == "CAT":
            chesire_cat_count += 1
print(chesire_cat_count)
