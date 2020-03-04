def Multiples_of_3_and_5(number_count):
    number = number_count -1
    multiple_list = 0
    while number != 0:
        if number % 3 == 0:
            multiple_list += number
        elif number % 5 == 0:
            multiple_list += number
        number -= 1
    print(multiple_list)
    return multiple_list


Multiples_of_3_and_5(1000)