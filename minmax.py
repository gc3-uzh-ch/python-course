#! /usr/bin/env python

class MinMax(object):
    """Compute the min and max of a streaming sequence."""

    def __init__(self, seq = None):
        if seq:
            self.min = min(seq)
            self.max = max(seq)
        else:
            self.min = None
            self.max = None


    def send(self, val):
        if (self.min is None) or (val < self.min):
            self.min = val
        if (self.max is None) or (val > self.max):
            self.max = val


class MinMaxAvg(object):
    """Compute the min and max of a streaming sequence."""

    def __init__(self, seq = None):
        if seq:
            self.min = min(seq)
            self.max = max(seq)
            self.__sum = float(sum(seq))
            self.__num = len(seq)
            self.avg = self.__sum/self.__num
        else:
            self.min = None
            self.max = None
            self.avg = None
            self.__sum = 0.0
            self.__num = 0

    def send(self, val):
        if (self.min is None) or (val < self.min):
            self.min = val
        if (self.max is None) or (val > self.max):
            self.max = val
        self.__sum += val # self.__sum = self.__sum + val
        self.__num += 1
        self.avg = self.__sum/self.__num


# usage examples
if __name__ == '__main__':
    f = MinMax()
    f.send(0)
    assert f.min == 0
    assert f.max == 0
    f.send(1)
    f.send(2)
    assert f.min == 0
    assert f.max == 2
