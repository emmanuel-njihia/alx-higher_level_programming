#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    function that replaces all occurrences of an element
    by another in a new list.
    '''
    if len(my_list) == 0:
        return my_list

    new_lst = [elem if elem != search else replace for elem in my_list]
    return new_lst
