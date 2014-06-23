#!/usr/bin/env python
# -*- coding: utf-8 -*-# 
# @(#)rt2.py
# 
# 
# Copyright (C) 2014, GC3, University of Zurich. All rights reserved.
# 
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

__docformat__ = 'reStructuredText'
__author__ = 'Antonio Messina <antonio.s.messina@gmail.com>'

def avg_rt_parametric(fname, condition='easy', correct=1):
    """Reads the database file `fname` and returns the average response
    time for condition `condition`.

    By defaults it will returns the average of the correct answer, but
    if called with `correct=0` it will returns the average of the
    *wrong* answers.
    """
    stream = open(fname)
    values = []
    for line in stream:
        cond, corr, rt = line.split()

        if cond != condition:
            continue

        if int(corr) != correct:
            continue

        values.append(float(rt))
    stream.close()
    return sum(values)/len(values)

if __name__ == "__main__":
    avgrt = avg_rt_parametric('rt.tsv')
    avgrt2 = avg_rt_parametric('rt.tsv', correct=0)
    avgrt3 = avg_rt_parametric('rt.tsv', condition='hard', correct=1)

    assert avgrt - 1.555927 < 1e-6
    print("Average RT for 'easy', 'correct' is: %f" % avgrt)

    assert avgrt2 - 2.10418064333 < 1e-6
    print("Average RT for 'easy', 'incorrect' is: %f" % avgrt2)

    assert avgrt3 - 3.5831878768 < 1e-6
    print("Average RT for 'hard', 'correct' is: %f" % avgrt3)
