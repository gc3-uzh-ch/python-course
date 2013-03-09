#!/usr/bin/env python
def load_data(filename):
    """
    Write a function load_data(filename) that reads a file containing
    one integer number per line, and return a list of the integer values.
    """
    fd = open(filename)
    data = fd.read()
    fd.close()

    values = []
    for num in data.split():
        values.append(int(num))

    return values

if __name__ == "__main__":
    data = load_data('values.dat')
    assert data == [299850, 299740, 299900, 300070, 299930]

