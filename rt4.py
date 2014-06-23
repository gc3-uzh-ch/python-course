#!/usr/bin/env python
# -*- coding: utf-8 -*-# 
# @(#)rt4.py
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

def parse_data(fname):
    """Read the database file `fname` and returns a dictionary with the
    values grouped by the `condition` parameter:

    { `condition`: [(`correct`, `rt`),
                    (`correct`, `rt`), ...] }

    `condition` is one of ['easy', 'medium', 'hard']
    `correct` is one of [0, 1]
    `rt` is a floating number

    """
    stream = open(fname)
    data = {}
    for line in stream:
        try:
            cond, corr, rt = line.split()
        except ValueError:
            print("Ignoring line '%s' as it is incorrectly formatted" % line.strip())
            continue

        try:
            newval = (int(corr), float(rt))
        except ValueError:
            print("Ignoring line '%s' as it has non-numerical values" % line.strip())
            continue

        if cond not in data:
            data[cond] = [newval]
        else:
            data[cond].append(newval)
    stream.close()
    return data


def avg_rt(data, condition='easy', correct=1):
    """
    `data` is a dictionary {`condition`: [(`correct`, `rt`), ]}

    Returns the average response time for the given parameters
    `condition` and `correct`.
    """

    subset = data[condition]
    values = []
    for corr, rt in subset:
        if correct == corr:
            values.append(rt)
    return sum(values)/len(values)

def analyze_data(data, condition='easy', max_rt=1e100):
    """Returns the number of correct answer in the dataset `data`, where
    condition is `condition` and the maximum response time is lesser
    than `max_rt`
    """
    subset = data[condition]
    correct = 0
    for corr, rt in subset:
        if rt > max_rt or corr == 0:
            continue
        correct += 1
    return correct


if __name__ == "__main__":
    fname = 'rt.dirty.tsv'
    maxrt = 1e100
    cond='easy'
    data = parse_data(fname)
    print("Nr. of correct answer for condition %s: %d" % (cond, analyze_data(data, condition=cond, max_rt=maxrt)))

    cond='hard'
    print("Nr. of correct answer for condition %s: %d" % (cond, analyze_data(data, condition=cond, max_rt=maxrt)))

    maxrt = 3.5
    cond='hard'
    print("Nr. of correct answer for condition %s with RT lesser than %.1f: %d" % (cond, maxrt, analyze_data(data, condition=cond, max_rt=maxrt)))
