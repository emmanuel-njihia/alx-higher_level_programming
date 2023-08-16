#!/usr/bin/python3
'''function that returns the number of keys in a dictionary'''


def number_keys(a_dictionary):
    num1 = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num1 += 1

    return (num1)
