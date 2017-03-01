# -*- coding: utf-8 -*-
# @Date    : 2017-02-27 11:32:01
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercixe 10 of HWPython

import os

tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."
teststring = "%r \n %s"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persion_cat)
print (backslash_cat)
print (fat_cat)
print (teststring % ('this is the /r permeter', "this this the /s permeter"))
