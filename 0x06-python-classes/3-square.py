#!/usr/bin/python3
'''
Class with a method
'''


class Square:
    '''
    square with a get area method
    '''

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integerr")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
