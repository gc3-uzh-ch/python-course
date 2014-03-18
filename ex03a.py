#!/usr/bin/env python

"""
    Write a function \texttt{odd} that takes a list of integers and
    returns a list of all the odd ones.
"""

def odd(lst):
    result = []
    for i in lst:
        if i % 2 == 1:
            result.append(i)
    return result

if __name__ == "__main__":
    assert odd([1,2,3,4, -3]) == [1,3, -3]

