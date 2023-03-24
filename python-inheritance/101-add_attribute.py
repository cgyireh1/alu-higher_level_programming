#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, attribute, value):
    """
    Args:
        obj (any): object to have attribute set
        attribute (str): name of new/updated attribute
        value (any): value to set to attribute
    Raises:
        TypeError: If adding or updating attribute not possible.
    """
    if hasattr(obj, "__dict__"):
        # if __dict__ is present, attributes can be dynamically added
        setattr(obj, attribute, value)
    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        # even if no __dict__, existing attributes in __slots__ can be updated
        setattr(obj, attribute, value)
    else:
        # out of options, can't add
        raise TypeError("can't add new attribute")
