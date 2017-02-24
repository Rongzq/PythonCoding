# -*- coding: utf-8 -*-
# @Date    : 2017-02-24 16:43:03
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 06 of HWPython

import os

x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "There who know %s and those who %s." % (binary, do_not)

print (x)
print (y)
print ('\n')
print ("I said: %r " % x)
print ("I also side: '%s' " % y)
print ('\n')
hilarious = False
joke_evaluation = "Isn't that joke os funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)