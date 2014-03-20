#!/usr/bin/env python

import re

class Grep(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def match(self, line):
        return re.search(self._pattern, line)

    def result(self, match, line):
        return line

    def next(self):
        line = next(self._file)
        match = self.match(line)
        while not match:
            line = next(self._file)
            match = self.match(line)
        return self.result(match, line)

    def __next__(self):
        """Compatibility method for Python 3"""
        return self.next()

class GrepOnlyMatching(Grep):

    def result(self, match, line):
        return match.group(0)


class GrepExactly(Grep):

    def match(self, line):
        return (self._pattern in line)


if __name__ == '__main__':
    # test Grep
    grep = Grep(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching(Grep):\n' == next(grep)
    assert 'class GrepExactly(Grep):\n' == next(grep)


    # test GrepOnlyMatching
    grep = GrepOnlyMatching(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching' == next(grep)
    assert 'class GrepExactly' == next(grep)

    # test GrepExactly
    grep = GrepExactly(__file__, 'class Grep')
    assert 'class Grep(object):\n' == next(grep)
    assert 'class GrepOnlyMatching(Grep):\n' == next(grep)
    assert 'class GrepExactly(Grep):\n' == next(grep)
