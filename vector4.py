#! /usr/bin/python

class Vector(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def mul(self, scalar):
    return Vector(scalar*self.x, scalar*self.y)
  def __str__(self):
    return ("<%g,%g>" % (self.x, self.y))
  def __eq__(self, other):
    return (self.x == other.x) and (self.y == other.y)
  def __add__(self, other):
    return Vector(self.x+other.x, self.y+other.y)


if __name__ == '__main__':
    v1 = Vector(0,1)
    v2 = Vector(1,0)
    assert v1 + v2 == Vector(1,1)
