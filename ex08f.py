#!/usr/bin/env python

import re

class GrepExactly(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def __iter__(self):
        return self

    def next(self):
        line = next(self._file)
        while self._pattern not in line:
            line = next(self._file)
        return line

    def __next__(self):
        """Compatibility method for Python 3"""
        return self.next()


if __name__ == '__main__':
    # test GrepExactly
    grep = GrepExactly(__file__, 'class Grep')
    assert 'class GrepExactly(object):\n' == next(grep)
