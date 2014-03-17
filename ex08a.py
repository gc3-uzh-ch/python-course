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

  def to_power(self, exponent):
    """
    Raise this complex number to integer power `exponent`.
    Non-recursive version.
    """
    z = ComplexNum(1,0)
    for i in range(exponent):
      z = z*self
    return z

  def to_power_recursive(self, n):
    """
    Raise this complex number to integer power `n`.
    Recursive version; i.e., use mathematical definition of exponentiation.
    """
    if n == 0:
        return ComplexNum(1,0)
    else:
        return self*self.to_power_recursive(n-1)


if __name__ == '__main__':
    z = ComplexNum(1,1)

    # z^0 is 1
    assert z.to_power(0) == ComplexNum(1,0)

    # z^1 is z
    assert z.to_power(1) == z

    # for small powers, we can spell out the product in full
    assert z.to_power(2) == z*z
    assert z.to_power(3) == z*z*z

    ## same set of tests, but for the "recursive" version

    # z^0 is 1
    assert z.to_power_recursive(0) == ComplexNum(1,0)

    # z^1 is z
    assert z.to_power_recursive(1) == z

    # for small powers, we can spell out the product in full
    assert z.to_power_recursive(2) == z*z
    assert z.to_power_recursive(3) == z*z*z
