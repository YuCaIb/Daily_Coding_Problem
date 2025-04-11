import random

# to obtain random lists
random_list = []

for i in range(4):
    rand = random.randint(1, 10)
    random_list.append(rand)

print(random_list)


# my_list=[1, 2, 3, 4, 5]

def multiply_exclude(rand_list):
    """
    for every index,
     multiply each element except the selected index of rand_list and appends multiplication it in to a new_list as a element.
      iterates for each index.

       returns the new list.

    :param rand_list:  of numbers
    :return: New list where each element is the product of all elements except the current index
    """
    new_list = []
    multiply = 1
    # to not to overlap indexes we need to accses indexes
    for i in range(len(rand_list)):
        for j in range(len(rand_list)):
            if i != j:
                multiply = multiply * rand_list[j]
        new_list.append(multiply)
        multipy = 1

    return new_list



my_list = multiply_exclude(random_list)
print(my_list)
