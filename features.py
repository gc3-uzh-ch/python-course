#! /usr/bin/python

class Features(object):
    """Compute the min and max of a streaming sequence."""

    def __init__(self, seq=[]):
        self.min = min(*seq)
        self.max = max(*seq)

    def send(self, val):
        if (self.min is None) or (val < self.min):
            self.min = val
        if (self.max is None) or (val > self.max):
            self.max = val

# usage examples
if __name__ == '__main__':
    f = Features()
    f.send(0)
    assert f.min == 0
    assert f.max == 0
    f.send(1)
    f.send(2)
    assert f.min == 0
    assert f.max == 2
