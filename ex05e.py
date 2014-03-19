#!/usr/bin/env python

"""
    Write a function `wordcount(filename)` that reads a text file and
    returns a dictionary, mapping words into occurrences (disregarding
    case) of that word in the text.  For the purposes of this
    exercise, a ``word'' is defined as a sequence of letters and the
    character ``-'', i.e., ``e-mail'' and ``more-or-less'' should both
    be counted as a single word.
"""

import string

def wordcount(filename):
    # read text from file
    fd = open(filename, 'r')
    rawtext = fd.read()
    fd.close()

    # split into list of words
    count = {}
    for word in rawtext.split():
        # convert to lowercase
        lcword = word.lower()
        # remove non-alphabetic characters
        cleanword = lcword.strip(string.punctuation)
        # count
        if cleanword not in count:
            count[cleanword] = 0
        count[cleanword] += 1

    return count

if __name__ == '__main__':
    wc = wordcount('lorem_ipsum.txt')
    assert wc['and'] == 3
    assert wc['more-or-less'] == 1
    assert wc['their'] == 2
    assert wc['infancy'] == 1
