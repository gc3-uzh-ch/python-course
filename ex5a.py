#!/usr/bin/python

class MinMax (object):
    """
    Change the MinMax class so that it can
    be initialized with a sequence; the .min and .max
    attributes should be initialized to the minimum and
    maximum of that sequence.
    
    Example:
    >>> m = MinMax([1,2,3])
    >>> m.min == 1
    True
    >>> m.max == 3
    True
    """

    def __init__(self, startseq = None):
        if startseq:
            self.min = min(startseq)
            self.max = max(startseq)
        else:
            self.min = None
            self.max = None

    def send(self, val):
        if (self.min is None) or (val < self.min):
            self.min = val
        if (self.max is None) or (val > self.max):
            self.max = val

if __name__ == "__main__":
    m = MinMax([1, 2, 3])
    assert m.min == 1
    assert m.max == 3
