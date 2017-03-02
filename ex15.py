# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 15:15:43
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 15 of HWPthon, 读取文件

import os
from sys import argv

script, filename = argv
txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input(">")
txt_again = open(file_again)

print (txt_again.read())
print (txt_again.close()) #在关闭文件之后打印出来的内容为"None", variable.open()/close() 打开关闭文件
# print (txt_again.read()) #文件在关闭之后再打印它的内容会有报错.