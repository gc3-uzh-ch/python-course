#!/usr/bin/env python
"""
    Read the documentation for the \texttt{dict.items} method, and
    give a solution of exercise \textbf{C} using multiple assignment
    and \texttt{dict.items}.
"""

def invert(D):
    invD = {}
    for key, value in D.items():
        invD[value] = key
    return invD

if __name__ == "__main__":
    assert invert({'a':'aaa','b':'bbb'}) == {'aaa':'a', 'bbb':'b'}
