# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 15:02:07
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 14 of HWPython, 提示和传递

import os
from sys import argv

script, user_name, code = argv
prompt = '>'

print ("Hi %s, I'm the %s script, I'm %r code" % (user_name, script, code))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s \n" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?\n")
computer = input(prompt)

print ("""
Alright, so you said %r about likeing me.\n
You live in %r. not sure where that is.\n
And you have a %r computer. Nice.\n	
	""" % (likes, lives, computer))
