#! -*- coding: utf8 -*-
from .singer import Singer

_singer_instance = Singer()

def sing(number):
    """Utility function for easier usage"""
    return _singer_instance.sing(number)
