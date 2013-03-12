#! /usr/bin/env python

"""
Usage: python rename.py EXT1 EXT2 DIR [DIR ...]

Rename all files in DIR, that end in EXT1 to end in EXT2 instead.
Repeat for all directory paths DIR given on the command line.
"""

# file name manipulation
import os
import os.path

# command-line arguments
import sys


# note that `sys.argv[0]` is always the script name, so actual
# arguments start at `sys.argv[1]`
if len(sys.argv) < 4:
    # not enough arguments, print usage message and exit
    print("""
Usage: python rename.py EXT1 EXT2 DIR [DIR ...]

Rename all files in DIR, that end in EXT1 to end in EXT2 instead.
Repeat for all directory paths DIR given on the command line.
""")
    sys.exit(1)

# now we know that sys.argv[1] and sys.argv[2] exists
ext1 = sys.argv[1]
ext2 = sys.argv[2]

# the DIR arguments are in `sys.argv[3]` and following elements
for dirname in sys.argv[3:]:
    entries = os.listdir(dirname)
    # `os.listdir()` returns just file names; make a full path by
    # re-adding the directory path in front
    paths = [ (dirname + '/' + entry) for entry in entries ]
    for path in paths:
        if path.endswith(ext1):
            # the new path is formed by removing the EXT1 at the end
            # and concatenating EXT2
            new_path = path[:-len(ext1)] + ext2
            # we're all set for the rename
            print ("Renaming '%s' to '%s' ..." % (path, new_path))
            #os.rename(path, new_path)
