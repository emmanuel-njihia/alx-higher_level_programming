#!/usr/bin/python3


def magic_calculation(a, b):
    results = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise ValueError('Value of k is too large')
            else:
                results += (a ** b) / k
        except ValueError:
            results = b + a
            break
    return results
