#!/usr/bin/python3
'''
Defining class
'''


class Square:
    '''
    class size value and type exeptions
    '''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
