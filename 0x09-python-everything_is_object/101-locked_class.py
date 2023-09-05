#!/usr/bin/python3
"""class defines a locked class."""


class LockedClass:
    """
    Prevents user from instantiating new LockedClass attributes
    for anything else unless  attributes referred as 'first_name'.
    """

    __slots__ = ["first_name"]
