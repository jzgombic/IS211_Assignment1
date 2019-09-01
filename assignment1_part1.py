#!/usr/bin/env python
# -*- coding: utf-8 -*-

def listDivide(numbers, divide=2):
    """The function returns the number of elements
    in the numbers list that are divisibleby divide.

    Args:
        numbers(list): a list of integers.
        divide (int): an integer with a default value of 2.

    Returns:
        int: the number of elements in the numbers list that
            are divisible by divide.

    Examples:
        >>> listDivide([1,2,7,12])
        2
        >>> listDivide([3,6,9,12,18,36], 6)
        4
    """
    
    count = 0
    for item in numbers:
        if item % divide is 0:
            count += 1
    return count
    testlistdivide()

class ListDivideException(Exception):
    pass


def testListDivide():
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException
    elif listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException
    elif listDivide([30, 54, 63, 98, 100], 10) != 2:
        raise ListDivideException
    elif listDivide([]) != 0:
        raise ListDivideException
    elif listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException
