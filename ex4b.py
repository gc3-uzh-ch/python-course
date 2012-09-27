#!/usr/bin/python

"""
Write a program that reads the euro.csv file, and populates a
dictionary from it: currency names (first column) are the dictionary
keys, conversion rates (second column) are the dictionary values.
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
    assert currencies['ITL'] == 1936.27
