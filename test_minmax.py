#! /usr/bin/env python

# stdlib imports
import unittest as ut

# local imports
from minmax import MinMax

class TestMinMax(ut.TestCase):

    def test_init(self):
        m = MinMax()
        self.assertEqual(m.min, None)
        self.assertEqual(m.max, None)

    def test_send0(self):
        m = MinMax()
        m.send(0)
        self.assertEqual(m.min, 0)
        self.assertEqual(m.max, 0)

    def test_send42(self):
        m = MinMax()
        m.send(0)
        m.send(42)
        self.assertEqual(m.min, 0)
        self.assertEqual(m.max, 42)

if __name__ == '__main__':
    ut.main()
