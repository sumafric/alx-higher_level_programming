#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for a in set(my_list):
        sum += a
    return sum
