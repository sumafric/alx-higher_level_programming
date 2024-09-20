#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {a: (a_dictionary[a] * 2) for a in a_dictionary}
    return new_dictionary
