# -*- coding: utf-8 -*-
# @Date    : 2017-02-27 14:40:01
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 13 of HWPython 参数, 解包和变量

import os
from sys import argv

#script, first, second, 
(script, first, second, third) = argv

#print ("The script is called: ", script)
#print ("Your first varible is: ", first)
#print ("Your second varible is: ", second)
print ("Your third varible is: ", third)