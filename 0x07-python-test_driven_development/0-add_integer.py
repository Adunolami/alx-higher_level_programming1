#!/usr/bin/python3
    """Adds two integer"""

    def add_integer(a, b=98):
        """Returns the integer addition of a and b.

        Float arguments are typecasted to int before addition is done.

        Raises:
            TypeError: if a or b is not an  an integer or float
        """

        if ((not isinstance(a, int) and not isinstance(a, float))):
            raise TypeError("a must be an integer")
        if ((not isinstance(b, int) and not isinstance(b, float))):
            raise TypeError("b must be an integer")
        return (int(a) + int(b)
