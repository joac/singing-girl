#! -*- coding: utf8 -*-
from __future__ import print_function
from .singer import Singer

_singer_instance = Singer()

def sing(number):
    """Utility function for easier usage"""
    return _singer_instance.sing(number)


if __name__ == '__main__':

    t = Singer()
    print(t.sing(1000000))




