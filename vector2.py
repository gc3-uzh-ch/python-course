#! /usr/bin/python

class Vector(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def add(self, other):
    return Vector(self.x+other.x, self.y+other.y)
  def mul(self, scalar):
    return Vector(scalar*self.x, scalar*self.y)
  def __str__(self):
    return ("<%g,%g>" % (self.x, self.y))


if __name__ == '__main__':
    v = Vector(0,1)
    assert str(v) == '<0,1>'
