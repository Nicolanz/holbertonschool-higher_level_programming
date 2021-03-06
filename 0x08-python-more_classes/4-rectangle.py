#!/usr/bin/python3
"""Module to define a rectangle object"""


class Rectangle:
    """Builder of the object"""
    def __init__(self, width=0, height=0):
        """Initializes attributes

        Keyword Arguments:
            width {int} -- [width of the rectangle] (default: {0})
            height {int} -- [height of the rectangle] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width to modify it

        Returns:
            [int] -- [width]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Modifies or assign width value

        Arguments:
            value {[int]} -- [self and value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return height to modify it

        Returns:
            [int] -- [height]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Assign or modify height value

        Arguments:
            value {[int]} -- [height value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of rectangle

        Returns:
            [int] -- [area]
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle

        Returns:
            [int] -- [perimeter]
        """
        if (self.width == 0 or self.height == 0):
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a string of the object

        Returns:
            [str] -- [String of the object]
        """
        string = ""
        if (self.__width == 0 or self.__height == 0):
            return (string)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                if (i < self.height - 1):
                    string += "\n"
            return (string)

    def __repr__(self):
        """Return strinf repr to create a new object

        Returns:
            [str] -- [String of the object]
        """
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))
