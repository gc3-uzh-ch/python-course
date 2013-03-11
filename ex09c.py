#!/usr/bin/env python

import re

## exercise 6C
class GrepExactly(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def __iter__(self):
        return self

    def next(self):
        line = self._file.next()
        while self._pattern not in line:
            line = self._file.next()
        return line


if __name__ == '__main__':
    # test GrepExactly
    grep = GrepExactly(__file__, 'class Grep')
    assert 'class Grep(object):\n' == grep.next()
    assert 'class GrepOnlyMatching(object):\n' == grep.next()
    assert 'class GrepExactly(object):\n' == grep.next()
