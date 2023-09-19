#!/usr/bin/python3
"""square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a new Square.

        Args:
            size (int): size of the new Square.
            x (int):  the x coordinate.
            y (int): The y coordinate.
            id (int): the new Square identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the Square.

        Args:
            *args (ints): New attribute values.
                - This 1st argument = id
                - 2nd argument = size
                - 3rd argument = x attribute
                - 4th argument = y attribute
            **kwargs (dict): New value pairs .
        """
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.size = arg
                elif b == 2:
                    self.x = arg
                elif b == 3:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for j, v in kwargs.items():
                if j == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif j == "size":
                    self.size = v
                elif j == "x":
                    self.x = v
                elif j == "y":
                    self.y = v

    def to_dictionary(self):
        """method return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """method returns the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
