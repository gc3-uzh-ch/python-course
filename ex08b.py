#! /usr/bin/env python

from vector_and_complexnum import Vector

class ComplexNum(Vector):
  "A complex number z = z1 + i * z2."
  def __mul__(self, other):
    if isinstance(other, ComplexNum):
        return ComplexNum(
            self.x*other.x - self.y*other.y,
            self.x*other.y + self.y*other.x)
    elif isinstance(other, (int, float)):
        return Vector.__mul__(self, other)
    else:
        raise RuntimeError("Can only multiply a ComplexNum by another ComplexNum or a built-in number type!")
  def __str__(self):
    return ("%g + i%g" % (self.x, self.y))


if __name__ == '__main__':
    z = ComplexNum(1,1)

    # scalar multiplication
    assert z * 2 == ComplexNum(2,2)

    # complex multiplication
    assert z * z == ComplexNum(0,2)
