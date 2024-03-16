#!/usr/bin/python3
"""
This module defines
the sqaure class and methods
"""


class Square:
    """
    Defines a square class with
    private instance attribute size
    and make validations
    to accept only positive integers
    for size and must be greater than 0
    """

    def __init__(self, size=0):
        """Initialize with private instance attribute size"""
        self.__size = size
        try:
            if self.__size is int:
                pass
        except TypeError:
            raise TypeError("size must be an integer")
        try:
            if self.__size < 0:
                pass
        except ValueError:
            raise ValueError("size must be >= 0")
