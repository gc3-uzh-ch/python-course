#!/usr/bin/env python

import re

class Grep(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def __iter__(self):
        return self

    def next(self):
        line = next(self._file)
        while not re.search(self._pattern, line):
            line = next(self._file)
        return line

    def __next__(self):
        """Compatibility method for Python 3"""
        return self.next()


if __name__ == '__main__':
    # test Grep
    grep = Grep(__file__, 'class Grep.*')
    assert 'class Grep(object):\n' == next(grep)
