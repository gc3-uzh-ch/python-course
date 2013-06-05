import re

class Grep(object):
    def __init__(self, filename, pattern):
        self._stream = open(filename, 'r')
        self._pattern = pattern

    def next(self):
        for line in self._stream:
            if re.search(self._pattern, line):
                return line

class GrepOnlyMatching(object):
    def __init__(self, filename, pattern):
        self._stream = open(filename, 'r')
        self._pattern = pattern

    def next(self):
        for line in self._stream:
            m = re.search(self._pattern, line)
            if m is not None:
                return m.group(0)

class GrepExactly(object):
    def __init__(self, filename, pattern):
        self._stream = open(filename, 'r')
        self._pattern = pattern

    def next(self):
        for line in self._stream:
            if self._pattern in line:
                return line
