#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number > 0:
        last = number % 10
        print("{}".format(last), end='')
        return (last)
    elif number < 0:
        last = (-number % 10)
        print("{}".format(last), end='')
        return (last)
    else:
        print("{}".format(last), end='')
        return (last)
