# -*- coding: utf-8 -*-
# @Date    : 2017-02-27 10:47:47
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 08 of HWPython

import os

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, True, False))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight")
	)
 