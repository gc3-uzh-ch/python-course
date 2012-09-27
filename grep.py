#! /usr/bin/env python

import re

class Grep(object):

    def __init__(self, filename, pattern):
        self._file = open(filename, 'r')
        self._pattern = pattern

    def __iter__(self):
        return self

    def match(self, line):
        return re.search(self._pattern, line)

    def result(self, match, line):
        return line

    def next(self):
        line = self._file.next()
        match = self.match(line)
        while not match:
            line = self._file.next()
            match = self.match(line)
        return self.result(match, line)


class GrepOnlyMatching(Grep):

    def result(self, match, line):
        return match.group(0)


class GrepExactly(Grep):

    def match(self, line):
        return (self._pattern in line)


if __name__ == '__main__':
    # test Grep
    grep = Grep(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching(Grep):\n' == grep.next()
    assert 'class GrepExactly(Grep):\n' == grep.next()


    # test GrepOnlyMatching
    grep = GrepOnlyMatching(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching' == grep.next()
    assert 'class GrepExactly' == grep.next()

    # test GrepExactly
    grep = GrepExactly(__file__, 'class Grep')
    assert 'class Grep(object):\n' == grep.next()
    assert 'class GrepOnlyMatching(Grep):\n' == grep.next()
    assert 'class GrepExactly(Grep):\n' == grep.next()
