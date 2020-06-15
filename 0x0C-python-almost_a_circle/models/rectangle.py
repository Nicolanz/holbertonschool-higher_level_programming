#!/usr/bin/python3
"""
Module of rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Args:
        Base ([class]): [parent class]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle construtor

        Args:
            width ([int]): [width]
            height ([int]): [height]
            x (int, optional): [x]. Defaults to 0.
            y (int, optional): [y]. Defaults to 0.
            id ([type], optional): [id]. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width gettter

        Returns:
            [int]: [width]
        """
        return self.__width

    @property
    def height(self):
        """height setter

        Returns:
            [int]: [height]
        """
        return self.__height

    @property
    def x(self):
        """x getter

        Returns:
            [int]: [x]
        """
        return self.__x

    @property
    def y(self):
        """y getter

        Returns:
            [int]: [y]
        """
        return self.__y

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value ([int]): [value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value ([int]): [value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """x setter

        Args:
            value ([int]): [value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """y setter

        Args:
            value ([int]): [value]

        Raises:
            TypeError: [Catchs type errors]
            ValueError: [Catchs value errors]
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Function to get te area of a rectangle

        Returns:
            [int]: [Rectangle's area]
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width):
                if j == 0:
                    for x in range(self.__x):
                        print(" ", end="")
                print('#', end="")
            if i is not self.__height:
                print()

    def __str__(self):
        """Returns the str way of the instance

        Returns:
            [str]: [String]
        """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Function to update values of intances
        """
        if args is not None:
            for key, value in kwargs.items():
                if key is "width":
                    self.__width = value
                elif key is "height":
                    self.__height = value
                elif key is "x":
                    self.__x = value
                elif key is "y":
                    self.__y = value
                elif key is "id":
                    self.id = value
                else:
                    break
        else:
            for i in range(len(args)):
                if i is 0:
                    self.id = args[i]
                elif i is 1:
                    self.__width = args[i]
                elif i is 2:
                    self.__height = args[i]
                elif i is 3:
                    self.__x = args[i]
                elif i is 4:
                    self.__y = args[i]
                else:
                    break

    def to_dictionary(self):
        """Return the dict repr of an rectangle

        Returns:
            [dict]: [dictionary]
        """
        dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return dict
