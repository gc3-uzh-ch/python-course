#! /usr/bin/env python

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


## exercise 6B
class GrepOnlyMatching(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def __iter__(self):
        return self

    def next(self):
        line = self._file.next()
        match = re.search(self._pattern, line)
        while not match:
            line = self._file.next()
            match = re.search(self._pattern, line)
        return match.group(0)


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
    # test Grep
    grep = Grep(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching(object):\n' == grep.next()
    assert 'class GrepExactly(object):\n' == grep.next()


    # test GrepOnlyMatching
    grep = GrepOnlyMatching(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching' == grep.next()
    assert 'class GrepExactly' == grep.next()

    # test GrepExactly
    grep = GrepExactly(__file__, 'class Grep')
    assert 'class Grep(object):\n' == grep.next()
    assert 'class GrepOnlyMatching(object):\n' == grep.next()
    assert 'class GrepExactly(object):\n' == grep.next()
