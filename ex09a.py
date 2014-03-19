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
