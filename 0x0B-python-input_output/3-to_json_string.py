#!/usr/bin/python3
""" Module that contains a function that returns the JSON
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON"""
    return json.dumps(my_obj)
