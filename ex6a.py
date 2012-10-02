#!/usr/bin/env python

import re

## exercise 6A
class Grep(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def __iter__(self):
        return self

    def next(self):
        line = self._file.next()
        while not re.search(self._pattern, line):
            line = self._file.next()
        return line


if __name__ == '__main__':
    # test Grep
    grep = Grep(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching(object):\n' == grep.next()
    assert 'class GrepExactly(object):\n' == grep.next()
