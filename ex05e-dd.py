#! /usr/bin/env python

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
    """
    Read `filename` and return a dictionary mapping each word into the
    corresponding count of occurrences within the contents of
    `filename`.

    This solution was contributed by Desislava Dimitrova
    at the Python course on March 19--20, 2014.
    """
    wc = {}

    # read file contents
    file_handle = open(filename,'r')
    contents = file_handle.read()
    contents = contents.lower()

    # replace punctuation with spaces
    for item in string.punctuation:
        if item == '-':
            continue
        contents = contents.replace(item,' ')

    # take unique words
    words = contents.split()
    words = set(words)

    # word counting
    for item in words:
        count = contents.count(item)
        wc[str(item)] = int(count)

    file_handle.close()

    return wc


if __name__ == '__main__':
    wc = wordcount('lorem_ipsum.txt')
    assert wc['and'] == 3
    assert wc['more-or-less'] == 1
    assert wc['their'] == 2
    assert wc['infancy'] == 1
