#!/usr/bin/env python

def invert(D):
    """
    Write a function invert(D) that takes a dictionary D and returns a
    dictionary Dinv with keys and values swapped. (We assume that D is
    1-1.)
    """
    invD = {}
    for key in D:
        value = D[key]
        invD[value] = key
    return invD

if __name__ == "__main__":
    assert invert({'a':'aaa','b':'bbb'}) == {'aaa':'a', 'bbb':'b'}
