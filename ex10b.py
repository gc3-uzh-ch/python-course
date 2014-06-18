#!/usr/bin/python

import re

class GrepExactly(object):
    def __init__(self, filename, pattern):
        self._stream = open(filename, 'r')
        self._pattern = pattern

    def next(self):
        while True:
            line = self._stream.next()
            if self._pattern in line:
                return line

if __name__ == '__main__':
    # test GrepExactly
    grep = GrepExactly(__file__, 'class Grep')
    assert 'class GrepExactly(object):\n' == grep.next()
