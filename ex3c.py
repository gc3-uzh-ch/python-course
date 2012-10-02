#!/usr/bin/env python

def maxarg(**kw):
    """
    Write a maxarg function, that takes
    arbitrary keyword arguments (but assume the values
    are all numbers), and returns the name of the
    argument with the largest value.
    """
    maxval = max(kw.values())
    for key in kw:
        if kw[key] == maxval:
            return key


if __name__ == "__main__":
    assert maxarg(a=1, b=2, c=-1) == 'b'
