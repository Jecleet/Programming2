'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing


# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)
'''
import re

def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

words = []

file = open('../Alice Spellcheck/dictionary.txt', 'r')
for line in file:
    for word in split_line(line):
        words.append(word.upper())
file.close()

def linear_spellcheck(input):
    print("---- Linear Spellcheck ----")
    linear_trigger = False
    for word in words:
        if input.upper() == word:
            linear_trigger = True
            return
    if linear_trigger == False:
        print(input)
        return(input)

def binary_spellcheck(input):
    print("---- Binary Spellcheck ----")
    lower_bound = 0
    upper_bound = len(words) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if words[middle_pos] < input.upper():
            lower_bound = middle_pos + 1
        elif words[middle_pos] > input.upper():
            upper_bound = middle_pos - 1
        else:
            found = True
            return
    if found == False:
        print(input)
        return(input)

linear_spellcheck("zzbrda")
binary_spellcheck("hello")



# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.

words_Alice_glass = []
words_Alice_Wonderland = []
not_shared_words = []

file = open('../Alice Spellcheck/AliceInWonderLand.txt', 'r')
for line in file:
    for word in split_line(line):
        words_Alice_Wonderland.append(word.upper())
file.close()

file = open('../Alice Spellcheck/AliceThroughTheLookingGlass.txt', 'r')
for line in file:
    for word in split_line(line):
        words_Alice_glass.append(word.upper())
file.close()

def binary_check(input, searched_list):
    lower_bound = 0
    upper_bound = len(searched_list) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if words[middle_pos] < input.upper():
            lower_bound = middle_pos + 1
        elif words[middle_pos] > input.upper():
            upper_bound = middle_pos - 1
        else:
            found = True
            return(True)
    if found == False:
        return(False)

words_Alice_Wonderland = list(set(words_Alice_Wonderland))
words_Alice_Wonderland.sort()
words_Alice_glass = list(set(words_Alice_glass))
words_Alice_glass.sort()

not_shared_words = [ x for x in words_Alice_glass if x not in words_Alice_Wonderland ]
print(not_shared_words)