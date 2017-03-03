# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 18:22:15
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 18 of HWPython, 命名, 变量, 代码和函数

import os


def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


def print_one(arg1):
    print("arg1: %r" % arg1)


def print_none():
    print("I got nothing.")


print_two("Rongzq", "jerry")
print_two_again("Rongzq", "Jerry")
print_one("First")
print_none()
