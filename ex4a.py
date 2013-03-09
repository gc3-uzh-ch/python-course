#!/usr/bin/env python

def cat(filename):
    """
    A function that prints the whole contents of a file.
    """
    fd = open(filename)
    data = fd.read()
    fd.close()
    print (data)

# alternatively, one can print the file line by line
def cat(filename):
    """
    A function that prints the whole contents of a file.
    """
    fd = open(filename)
    for line in fd:
        print(line)
    fd.close()
