#!/usr/bin/python3
"""Module to define a rectangle object"""


class Rectangle:
    """Builder of the object"""
    number_of_instances = 0
    print_symbol = '#'
    size = 0

    def __init__(self, width=0, height=0):
        """Initializes attributes

        Keyword Arguments:
            width {int} -- [width of the rectangle] (default: {0})
            height {int} -- [height of the rectangle] (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    string += str(self.print_symbol)
                if (i < self.height - 1):
                    string += "\n"
            return (string)

    def __repr__(self):
        """Return strinf repr to create a new object

        Returns:
            [str] -- [String of the object]
        """
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Prints message when object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares areas of instances

        Arguments:
            rect_1 {[int]} -- [Area of rect_1]
            rect_2 {[inr]} -- [Area of rect_2]

        Raises:
            TypeError: [Catchs type errors]
            TypeError: [Catchs type errors]

        Returns:
            [int] -- [the bigger area]
        """
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new object

        Keyword Arguments:
            size {int} -- [size] (default: {0})
        """
        return(cls(width=size, height=size))
