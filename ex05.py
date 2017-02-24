# -*- coding: utf-8 -*-
# @Date    : 2017-02-24 15:31:14
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 05 of HWPython
import os

name = 'Rongzq'
age = 35 #it is true
height = 74 #inches
weight = 180 #lbs
eye = 'Blue'
teeth = 'White'
hair = 'Brown'

print ("Let's talk about %r." % name)
print ("He's %f centermeter tall." %(height * 2.54))
print ("He's %f Kg heavy." %(weight * 0.4536))
print ("Actually that's not too heavy")
print ("He's got %s eyes and %r hair." %(eye, hair))
print ("His teeth are usually %s depending on the coffe." %teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %r I get %d." %(age, height, weight, age + height + weight))