#!/usr/bin/python3
def element_at(my_list, idx):
    if idx not in my_list or idx >= len(my_list):
        return ("None")
    return (my_list[idx])
