#!/usr/bin/python3
""" A square function with private instance attribute """


class Square:
    """ Define the square of number """
    def __init__(self, size):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
