#!/usr/bin/python

class MinMax (object):
    """
    Augment the MinMax class so that it computes the average of the
    numbers given to it via the send method. Store this average in the
    .average instance attribute.
    """

    def __init__(self):
        self.min = None
        self.max = None
        self.averate = None
        self.__values = []

    def send(self, val):
        self.__values.append(val)
        if (self.min is None) or (val < self.min):
            self.min = val
        if (self.max is None) or (val > self.max):
            self.max = val
        self.average = float(sum(self.__values))/len(self.__values)

if __name__ == "__main__":
    m = MinMax()
    m.send(1)
    m.send(2)
    m.send(3)
    assert m.min == 1
    assert m.max == 3
    assert m.average == 2
