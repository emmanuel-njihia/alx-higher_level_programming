#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num1 = 0
    den1 = 0

    for tup in my_list:
        num1 += tup[0] * tup[1]
        den1 += tup[1]

    return (num1 / den1)
