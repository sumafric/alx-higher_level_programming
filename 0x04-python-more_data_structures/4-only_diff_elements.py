#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    d_set  = (set_1 | set_2) - (set_1 & set_2)
    return d_set
