#!/usr/bin/python3
"""function that divides 2 integers and prints the integer and prints result"""

def safe_print_division(a, b):
    try:
        division = a / b
    except (TypeError, ZeroDivisionError):
        division = None
    finally:
        print("Inside result: {}".format(division))
        return (division)
