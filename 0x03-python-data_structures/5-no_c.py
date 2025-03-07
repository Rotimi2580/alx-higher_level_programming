#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    else:
        new_str = ""
        for i in my_string:
            if i == 'c' or i == 'C':
                continue
            else:
                new_str += i
        return (new_str)
