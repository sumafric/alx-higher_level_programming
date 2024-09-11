#!/usr/bin/python3
def remove_char_at(str, n):
    new_char = ""
    a = 0
    for char in str:
        if a != n:
            new_char += char
        a += 1
    return new_char
