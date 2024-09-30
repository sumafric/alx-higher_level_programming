#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a, elements = 0, 0
    try:
        for value in my_list:
            a += 1
            if a <= x:
                if isinstance(value, int):
                    print("{:d}".format(value), end="")
                    elements += 1
        print()
    except Exception:
        print("Error!")
    return elements
