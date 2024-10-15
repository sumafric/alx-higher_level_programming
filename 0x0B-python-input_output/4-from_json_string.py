#!/usr/bin/python3
""" Module that contains a function that returns an object - JSON rep"""
import json


def from_json_string(my_str):
    """ Function that returns an object - JSON representation"""
    return json.loads(my_str)
