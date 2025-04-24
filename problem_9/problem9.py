import random

my_list = []

for i in range(5):
    rand = random.randint(1, 10)
    my_list.append(rand)


def some_name(some_list, temp=0):
    # in the question it asks for non-adjenct,
    # first I felt like index 0 and index 1 shouldn't be like x, x+1
    # but as it seems according to instances, it means that just indexes.
    for i in range(len(some_list)):

        if i % 2 == 0:
            temp = some_list[i] + temp

    print(some_list)
    return temp


some_name(my_list)
