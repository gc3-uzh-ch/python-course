#!/usr/bin/env python

"""
Building upon the previous exercise, create a rates[][] 2D array that
stores the convertion rate of two currencies given the name, e.g.,
rate[’ITL’][’DEM’] gives the conversion rate of Italian Liras to
Deutsche Marks.
"""


def read_rates_from_file(filename):
    currencies = {}
    fd = open(filename)
    for line in fd:
        (name, rate) = line.split(',', 1)
        rate = float(rate)
        currencies[name] = rate
    fd.close()
    return currencies


if __name__ == "__main__":
    currencies = read_rates_from_file('euro.csv')

    rates = {}
    for key1 in currencies:
        rates[key1] = {}
        for key2 in currencies:
            rates[key1][key2] = currencies[key2]/currencies[key1]
    
