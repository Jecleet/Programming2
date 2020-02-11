# Searching

# use forward slashes to go into folders and .. to go "up" a folder
file = open('../resources/super_villains.txt', 'r')  # open to read
print(file)

for line in file:
    print(line.strip())

file.close()


# 'w' opens to write and overwrites the file
# 'a' opens to append
file = open('../resources/super_villains.txt', 'a')
file.write('Lee the Merciless\n')
file.write('Mia the horrible\n')
file.close()

# .strip() method removes the extra characters at end of text
print("    Hello ".strip())
print("World\n".strip())
print("!")

#  Better way to open close a file (syntactic sugar)
# file automatically closes after execution of with
with open('../resources/super_villains.txt') as f:
    for line in f:
        print(line.strip())


# .read() method just imports whole file as a string
with open('../resources/super_villains.txt') as f:
    read_data = f.read()  # big string

print("\n\nRead method")
print(read_data)

# Reading data into an array (list)
with open('../resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]

print(villains)

# Linear Search (not very efficient but easy)

key = "VARVARA TEMPEST"

i = 0
while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < len(villains) - 1:
    print("Found", key, "at position", i)
else:
    print(key, "not found")

def linear_search(key, list):
    for i in list:
        if i == key:
            position = list.index(i)
            return (True, position)
    return (False)


print(linear_search(key, villains))

import re #regular expression

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

my_text = "Hello, this is Aaron's phone!"
print(split_line(my_text))

file = open("../resources/alice_in_wonderland")

for line in file:
    line = line.strip().upper()
    words = split_line(line)