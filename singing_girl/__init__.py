#! -*- coding: utf8 -*-
from .singer import Singer


_singer_instance = Singer()


def sing(number):
    """Utility function for easier usage
    :param number: an integer, float or decimal number
    """
    return _singer_instance.sing(number)
