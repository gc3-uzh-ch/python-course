#!/usr/bin/env python

def zip2(tlist):
    """
    Implement a zip2 function, that takes a list of 2-tuples and
    returns two lists: a list of all the first items in the pairs, and
    a list of all the second items in the pairs.
    """
    list1 = []
    list2 = []
    for item1, item2 in tlist:
        list1.append(item1)
        list2.append(item2)
    return (list1, list2)

if __name__ =="__main__":
    tlist = [(1, '1',),
             (2, '2'),
             (3, '3'),
             ]
    assert zip2(tlist) == ([1,2,3], ['1','2','3'])
