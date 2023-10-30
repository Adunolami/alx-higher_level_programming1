#!/usr/bin/python3
    """Defines a  rectangle class"""
Class Rectangle:

    def __init__(self,width=0, height=0):

        """initialize a new Rectange
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self._width

    @width.setter

    def width(self, value):
        if not ininstance(value, int):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError ("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self._height

    @height.setter
    def height(self.value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
