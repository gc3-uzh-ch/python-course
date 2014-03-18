#!/usr/bin/env python

"""
    Write a function \texttt{odd} that takes a list of integers and
    returns a list of all the odd ones.
"""

def odd(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i)
    return result
