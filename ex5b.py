#!/usr/bin/env python

import math

class Vector(object):
  """
  Add a new method `norm` the `Vector` class: if
  `v` is an instance of class `Vector`, then calling
  `v.norm()` returns the norm (modulus) of the associated
  vector.

  Example:

    >>> v = Vector(3,4)
    >>> v.norm()
    5
  """
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def add(self, other):
    return Vector(self.x+other.x, self.y+other.y)
  def mul(self, scalar):
    return Vector(scalar*self.x, scalar*self.y)
  def show(self):
    return ("<%g,%g>" % (self.x, self.y))
  def norm(self):
    return math.sqrt(self.x**2 + self.y**2)
  def unit(self):
    norm = self.norm()
    return self.mul(1 / norm)

if __name__ == "__main__":
    v = Vector(3,4)
    u = v.unit()
    assert u.norm() == 1
