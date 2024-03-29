#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Custom int type inverting behavior of != and == operators.
    """

    def __eq__(self, other):
        """Reverses behavior of == operator.
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """Reverses behavior of != operator.
        """
        return int(self) == int(other)
