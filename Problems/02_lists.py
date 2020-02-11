# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(1, 101)]
#print(my_list)
# b) Make a list of even numbers from 20 to 40
my_list = [x for x in range(20,41) if x % 2 == 0]
print(my_list)

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x**2 for x in range(1,101)]
print(my_list)
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_other_list = [x for x in my_list if x > 0]
print(my_other_list)

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list
import number_list
for i in range(1, 6):
    print(number_list.num_list[-i])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(number_list.num_list))
# Find and print the lowest number in num_list (1pt)
print(min(number_list.num_list))
# Find and print the average of num_list (2pts)
print(sum(number_list.num_list)/len(number_list.num_list))
# Remove the lowest number from num_list (2pt)

value = number_list.num_list.index(min(number_list.num_list))
del number_list.num_list[value]


# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
my_list = number_list.num_list
top_ten = []
for i in range(10):
    max_variable = max(my_list)
    top_ten.append(max_variable)
    position = my_list.index(max_variable)
    del my_list[position]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
list_two = []
for i in number_list.num_list:
    value = number_list.num_list.count(i)
    list_two.append(value)
position = list_two.index(max(list_two))
print(number_list.num_list[position])


# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
"""
count = 0
for number in number_list.num_list:
    number_2 = int(number)
    for j in range(2, number_2/2): # this does not work but i do not understand why
        if number_list % j != 0:
            count += 1
            break

print("check")
print(count)
"""
# Find the number of palindromes
# Hint: This may be easier to do with strings
count = 0
for number in number_list.num_list:
    forward = str(number)
    backward = forward[::-1]
    if forward == backward:
        count += 1
print("check")
print(count)



