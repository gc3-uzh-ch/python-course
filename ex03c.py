#!/usr/bin/env python
"""
Assignment: Write a `maxarg` function, that takes arbitrary
keyword arguments, and returns the name of the argument with the
largest value.

You can assume:
- values in the dictionary are all numbers;
- all values are distinct
"""

# first solution: build on the `invert` function from ex03a.
from ex03a import invert
def maxarg1(**kw):
    D = invert(kw)
    m = max(* D.keys())
    return D[m]

# second solution: find the max, then loop on keys and values
# simultaneously to find the corresponding key
def maxargs2(**kw):
    maxval = max(* kw.values())
    for key, value in kw.items():
        if value == maxval:
            return key

# 3rd solution: loop again, but with no previous knowledge of what the
# maximum value is
def maxargs2(**kw):
    maxval = None
    the_key = None
    for key, value in kw.items():
        if (maxval is None) or (value > maxval):
            the_key = key
            maxval = value
    return the_key


if __name__ == "__main__":
    assert maxarg1(a=1, b=2, c=-1) == 'b'
    assert maxarg2(a=1, b=2, c=-1) == 'b'
    assert maxarg3(a=1, b=2, c=-1) == 'b'
    # { 'a':1, 'b':2, 'c':-1 }
