#!/usr/bin/python3

import sys
"""function that executes a function safely."""


def safe_function(fct, *args):
    try:
        results = fct(*args)
        return results
    except Exception as e:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
