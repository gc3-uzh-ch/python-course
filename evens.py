#! /usr/bin/env python

class Evens(object):
  """Iterate over the even numbers in a sequence."""

  def __init__(self, numbers):
    # transform sequence into an iterator
    self._numbers = iter(numbers)

  def next(self):
      # continue drawing numbers until we get an even one
      result = next(self._numbers)
      while (result % 2) != 0:
          result = next(self._numbers)
      return result

  def __next__(self):
      """Compatibility method for Python 3"""
      return self.next()

  def __iter__(self):
      return self


if __name__ == '__main__':
    e = Evens([1,2,3,5,7,8,10])
    e.next() == 2
    e.next() == 8
    e.next() == 10

    e = Evens([1,2,3,5,7,8,10])
    for i in e:
        print (i*i)
