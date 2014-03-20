#! /usr/bin/env python

class ReadPairs(object):

    def __init__(self, filename):
        self.fd = open(filename, 'r')

    def next(self):
        while True:
            # upon EOF, this also raises StopIteration so no need to
            # do it ourselves
            line = next(self.fd)
            values = line.split(",")
            if len(values) == 2:
                i = int(values[0])
                j = int(values[1])
                return (i, j)

    def __next__(self):
        """Compatibility method for Python 3"""
        return self.next()


    # must return an iterator, i.e., an object with a next() method
    def __iter__(self):
        return self


if __name__ == '__main__':
    wt = ReadPairs('wt.csv')

    # first well-formed lines of the file
    assert next(wt) == (1, 21)
    assert next(wt) == (128, 175)
