#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    elements = 0
    try:
        for value in my_list:
            a += 1
            if a <= x:
                print("{}".format(value), end="")
                elements += 1
        print()
    except Exception as error:
        print(error)
    return elements
