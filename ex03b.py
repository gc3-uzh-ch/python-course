#!/usr/bin/env python
"""
    Write a function \texttt{concat} that takes a list of lists and
    returns the concatenation of those lists.
"""

def concat1(lst):
    """
    Solution 1: using list operators
    """
    result = []
    for l in lst:
        result += l
    return result

def concat2(lst):
    """
    Solution 2: using nested loops
    """
    result = []
    for l in lst:
        for i in l:
            result.append(i)
    return result

if __name__ == "__main__":
    assert concat1([ [1,2,3], [4,5,6], [7,8,9] ]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]      
    assert concat2([ [1,2,3], [4,5,6], [7,8,9] ]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]      

