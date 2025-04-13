import random


def rand_int_list_ge(a=-10, b=10, limit=10):
    """
    produces a list of random integers between a and b.
    :param: a : lowest range
            b: highest range
    :return random int list in given range
    """
    my_list = []
    for i in range(limit):
        rand = random.randint(a=a, b=b)
        my_list.append(rand)
    return my_list


def bubble_sort(my_list):
    """
    bubble sort algorithm
    :param my_list:
    :return:
    """
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


this_list = rand_int_list_ge(-10, 10)
print(this_list)
print(bubble_sort(this_list))


def find_first_missing_int(unique: list):
    """

    :param unique: list of integers
    :return: prints unique elements and the first positive missing number (incresses 1 by 1)
    """

    unique = bubble_sort(list(set(unique)))
    for i in range(len(unique)):
        if unique[i] + 1 not in unique and unique[i] + 1 > 0:
            print(unique[i] + 1)
            print(unique)
            break


find_first_missing_int(this_list)

