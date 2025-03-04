#!/usr/bin/python3
from calculator_1 import mul, sub, add, div
if __name__ == "__main__":
    a = 10
    b = 5
    result = ["{} + {} = {}".format(a, b, add(a, b)), "{} - {} = {}".format(a, b, sub(a, b)), "{} * {} = {}".format(a, b, mul(a, b)), "{} / {} = {}".format(a, b, div(a, b))]
    for i in result:
        print("{}".format(i))
