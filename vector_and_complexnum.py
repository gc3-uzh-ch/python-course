#! /usr/bin/python

class Vector(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __eq__(self, other):
    return (self.x == other.x) and (self.y == other.y)
  def __add__(self, other):
    return self.__class__(self.x+other.x, self.y+other.y)
  def __mul__(self, scalar):
    return Vector(scalar*self.x, scalar*self.y)
  def __str__(self):
    return ("<%g,%g>" % (self.x, self.y))


class ComplexNum(Vector):
  def __mul__(self, other):
    return ComplexNum(
        self.x*other.x - self.y*other.y,
        self.x*other.y + self.y*other.x)
  def __str__(self):
    return ("%g + i%g" % (self.x, self.y))


if __name__ == '__main__':
    # Vector tests
    v1 = Vector(0,1)
    v2 = Vector(1,0)
    assert v1 + v2 == Vector(1,1)

    # ComplexNum tests
    z = ComplexNum(1,1)
    i = ComplexNum(0,1)
    u = ComplexNum(1,0)

    assert z == u + i
    assert isinstance(u+i, ComplexNum)

    assert z == z*u
    assert i == i*u

    assert i*i == ComplexNum(-1,0)
