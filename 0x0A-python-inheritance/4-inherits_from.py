#!/usr/bin/python3

"""Defines an inherited checking func."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance.
    If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
