#!/usr/bin/python3
''' function that returns a tuple with the length of a string and
its first character.'''


def multiple_returns(sentence):
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
