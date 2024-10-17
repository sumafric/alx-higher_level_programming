#!/usr/bin/python3

"""Defines class and inherited checking func."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance.
    If obj is an instance / inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
