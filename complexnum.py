#! /usr/bin/env python

class ComplexNum(object):
  "A complex number z = z1 + i * z2."
  def __init__(self, z1, z2):
    self.re = z1
    self.im = z2
  def __add__(self, other):
    return ComplexNum(
      self.re+other.re, self.im+other.im)
  def __mul__(self, other):
    return ComplexNum(
      self.re*other.re - self.im*other.im,
      self.re*other.im + self.im*other.re)
  def __str__(self):
    return ("%g + i%g" % (self.re, self.im))
  def __eq__(self, other):
    return (self.re == other.re) and (self.im == other.im)


if __name__ == '__main__':
    z = ComplexNum(1,1)
    i = ComplexNum(0,1)
    u = ComplexNum(1,0)

    assert z == u + i

    assert z == z*u
    assert i == i*u

    assert i*i == ComplexNum(-1,0)
