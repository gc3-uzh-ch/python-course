#! /usr/bin/python

class Vector(object):
  """
  Documentation on how to use the `Vector` class.

    >>> v = Vector(1, 2)

  All python code executed whitin the same docstring is executed in
  the same session, so that you can easily interleave python code and
  explanations.

    >>> print(v)
    <1,2>

  Vectors define two attributes, which are the `x` and `y`
  coordinates:

    >>> v.x
    1
    >>> v.y
    2

  You can add two vectors

    >>> v2 = Vector(2,3)
    >>> print(v + v2)
    <3,5>
  
  Multiply a vector for a scalar (the next test will fail)

    >>> print(v * 2)
    <2,1>

  please note that multiplication is NOT commutative:

    >>> print(2 * v)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'Vector'

  and of course you can check if two vectors are the same

    >>> Vector(1, 2) == Vector(1, 2)
    True
    >>> Vector(1, 2) == Vector(4, 5)
    false
  """
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __mul__(self, scalar):
    """
    Any docstring from any method will be searched for tests.

      >>> v = Vector(1, 2)
      >>> print(v * 2)
      <2,4>
    """
    return Vector(scalar*self.x, scalar*self.y)
  def __str__(self):
    return ("<%g,%g>" % (self.x, self.y))
  def __eq__(self, other):
    return (self.x == other.x) and (self.y == other.y)
  def __add__(self, other):
    return Vector(self.x+other.x, self.y+other.y)


if __name__ == '__main__':
  import doctest
  doctest.testmod()
