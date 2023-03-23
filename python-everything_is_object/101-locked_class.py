#!/usr/bin/python3
"""
Defines class with no class or object attribute
Control dynamically created instance attributes
"""


class LockedClass():
    """
    prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"

    c = LockedClass()
    c.first_name = 'Caroline'
    c.first_name
    'Caroline'

    c.last_name = 'Gy'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
