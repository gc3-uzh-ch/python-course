#!/usr/bin/env python

def maxarg(**kw):
    """
    Write a maxarg function, that takes
    arbitrary keyword arguments (but assume the values
    are all numbers), and returns the name of the
    argument with the largest value.
    """
    D = invert(kw)
    m = max(D.keys())
    return D[m]


if __name__ == "__main__":
    assert maxarg(a=1, b=2, c=-1) == 'b'
    # { 'a':1, 'b':2, 'c':-1 }
