#! /usr/bin/env python
#
# Solution contributed by Desislava Dimitrova
# at the Python course on March 19--20, 2014.
#


def wordcount(filename):
    import string

    dict = {}
    file_handle = open(filename,'r')
    string_temp = file_handle.read()
    string_temp = string_temp.lower()
    for item in string.punctuation:
        if item == '-':
            continue
        string_temp = string_temp.replace(item,' ')
    #cosmetic change
    string_temp = string_temp.replace('  ',' ')

    #take unique words
    list_temp = string_temp.split()
    list_temp = set(list_temp)

    #word counting
    for item in list_temp:
        count = string_temp.count(item)
        dict[str(item)] = int(count)
    print(dict)

    file_handle.close()
