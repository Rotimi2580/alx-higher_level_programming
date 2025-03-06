#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in _reversed(my_list):
            print("{:d}".format(i))

def _reversed(my_list=[]):
    new_list = [0] * len(my_list)
    for i in range(len(my_list)):
        if i >= 0:
            new_list[len(my_list) - 1 - i)] = my_list[i]
    return (my_list)
