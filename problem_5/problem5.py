# ~ I still couldn't understand the question does this talks about tuples ?? ~
import random


# So the question is basically asks what it asks. It asks to write down 2 functions that will write up first element
# of a tuple and another function that print out last element of the tuple.
#
def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


p = cons(random.randint(a=-10, b=10), random.randint(a=-10, b=10))  # randomizing the numbers so I could tell..


def car(pair):  # choosing the first element
    return pair(lambda a, b: a)  # choosing a


def cdr(pair):
    return pair(lambda a, b: b)  # choosing b


print(car(p))
print(cdr(p))
