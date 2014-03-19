#! /usr/bin/env python

class ReadPairs(object):

    def __init__(self, filename):
        self.fd = open(filename, 'r')

    def next(self):
        while True:
            # upon EOF, this also raises StopIteration so no need to
            # do it ourselves
            line = self.fd.next()
            values = line.split(",")
            if len(values) == 2:
                i = int(values[0])
                j = int(values[1])
                return (i, j)

    # must return an iterator, i.e., an object with a next() method
    def __iter__(self):
        return self


if __name__ == '__main__':
    wt = ReadPairs('wt.csv')

    # first well-formed lines of the file
    assert wt.next() == (1, 21)
    assert wt.next() == (128, 175)
