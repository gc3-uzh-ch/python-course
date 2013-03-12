#!/usr/bin/env python

def load_data(filename):
    """
    Write a function load_data(filename) that reads a file containing
    one integer number per line, and return a list of the integer values.
    """
    fd = open(filename)

    values = []
    for line in fd:
        line = line.strip()
        try:
            elt = int(line)
            values.append(elt)
        except:
            print ("load_data: Ignoring line '%s'" % line)

    return values


if __name__ == "__main__":
    data = load_data('test.csv')

    assert data == [1, 2, 3, 4]
