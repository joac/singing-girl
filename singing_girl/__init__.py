#! -*- coding: utf-8 -*-
from __future__ import print_function
from .singer import Singer


if __name__ == '__main__':

    t = Singer()
    print(t.sing(1000000))
