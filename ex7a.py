#! /usr/bin/env python

# stdlib module for filesystem operations
import os


def mkdir_p(path):
    """
    Create a directory at location `path`.
    If the directory already exists, do nothing.

    Return `True` or `False`, depending on whether
    a directory was created or not.
    """
    try:
        os.mkdir(path)
        return True
    except OSError:
        return False


if __name__ == '__main__':
    assert mkdir_p('/') == False
