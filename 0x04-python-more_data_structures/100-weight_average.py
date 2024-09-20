#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    _num = 0
    _den = 0
    if len(my_list) == 0:
        return 0
    for a in my_list:
        _num += (a[0] * a[1])
        _den += a[1]
    return _num / _den
