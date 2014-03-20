#!/usr/bin/env python

import re

class GrepOnlyMatching(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def __iter__(self):
        return self

    def next(self):
        line = next(self._file)
        match = re.search(self._pattern, line)
        while not match:
            line = next(self._file)
            match = re.search(self._pattern, line)
        return match.group(0)

    def __next__(self):
        """Compatibility method for Python 3"""
        return self.next()


if __name__ == '__main__':
    # test GrepOnlyMatching
    grep = GrepOnlyMatching(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching' == next(grep)
