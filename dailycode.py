"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

import random


def wheter_sum_equal(my_list: list, k: int):
    for i in enumerate(my_list):
        ## i is a tuple
        for j in enumerate(my_list):
            if i[0] != j[0]:
                if i[-1] + j[-1] == k:
                    print(str(i[-1]) + " + " + str(j[-1]) + f" is equal to {k}")


my_list = []

for i in range(10):
    rand = random.randint(1, 20)
    my_list.append(rand)

k = random.randint(1, 100)
print("this is the k : " + str(k))
print("this is the list" + str(my_list))

wheter_sum_equal(my_list, k)
