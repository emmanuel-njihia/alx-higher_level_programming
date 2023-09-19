#!/usr/bin/python3
"""This defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    " a rectangle child class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width.
            height (int): The height .
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The new Rectangle identity.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either  width or height <= 0.
            TypeError: If either  x or y is not an int.
            ValueError: If either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set th width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """sets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """print rectangle using '#'"""
        if self.width == 0 or self.height == 0:
            print("")
            [print("") for y in range(self.y)]
            for h in range(self.height):
                [print("", end="") for x in range(self.x)]
                [print("#", end="") for w in range(self.width)]
                print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle by
        overiding the ___str___ method.

        Args:
            *args (ints): New attribute values.
                - 1st argument = id attribute
                - 2nd argument = width
                - 3rd argument = height
                - 4th argument = x
                - 5th argument = y
            **kwargs (dict): New value pairs of attributes.
        """
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.width = arg
                elif b == 2:
                    self.height = arg
                elif b == 3:
                    self.x = arg
                elif b == 4:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for j, v in kwargs.items():
                if j == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif j == "width":
                    self.width = v
                elif j == "height":
                    self.height = v
                elif j == "x":
                    self.x = v
                elif j == "y":
                    self.y = v

    def to_dictionary(self):
        """dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """returns print() and str()
        of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
