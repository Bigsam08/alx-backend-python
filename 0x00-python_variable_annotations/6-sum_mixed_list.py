#!/usr/bin/env python3
''' A function that takes a mixed-list of int and
float to return the sum of float
'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' A function that takes a mixed-list of int and
    float to return the sum of float
    '''
    return sum(mxd_lst)
