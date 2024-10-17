#!/usr/bin/python3
"""Defines function is_same_class"""


def is_same_class(obj, a_class):
    """If obj is === an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
