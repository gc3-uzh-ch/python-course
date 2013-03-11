#!/usr/bin/env python

def shout(filename):
    """
    A function that returns the whole contents of a file with letters
    converted to uppercase.
    """
    contents = ''
    fd = open(filename)
    for line in fd:
        contents += line.upper()
    fd.close()
    return contents
