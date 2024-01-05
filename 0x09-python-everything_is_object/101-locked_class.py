#!/usr/bin/python3
class LockedClass:
    """
    prevent the user from instantating new lockedclass attributes
    for anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
