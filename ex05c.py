#!/usr/bin/env python
"""
  Write a function called `load_data2(filename, bound)`
  that, *using comprehensions*, reads a file containing one
  integer number per line, and return a list of the integer values
  *lesser than* `bond`.

"""

def load_data2(filename, bound):
    return [int(num) for num in open(filename) if int(num) < bound]

if __name__ == "__main__":
    data = load_data2('values.dat', 300000)
    assert data == [299850, 299740, 299900, 299930]

