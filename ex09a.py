#!/usr/bin/python

import re

class GrepOnlyMatching(object):
    def __init__(self, filename, pattern):
        self._stream = open(filename, 'r')
        self._pattern = pattern

    def next(self):
        for line in self._stream:
            m = re.search(self._pattern, line)
            if m is not None:
                return m.group(0)

if __name__ == '__main__':
    # test GrepOnlyMatching
    grep = GrepOnlyMatching(__file__, 'class Grep[A-Za-z]+')
    assert 'class GrepOnlyMatching' == grep.next()
