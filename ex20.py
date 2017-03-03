# -*- coding: utf-8 -*-
# @Date    : 2017-03-03 09:07:18
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 20 of HWPython, 函数和文件

import os
from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0, 0)


# f.readline()完成后最后一个字符是'\n', 此时光标已经定位在下一行的第0个位置
def print_a_line(line_count, fo):
    print(line_count, fo.readline())


current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)
line1 = current_file.readline()
line2 = current_file.readline()
line3 = current_file.readline()
print(line1)
print(line2)
print(line3)

print("Let's print three lines:")
rewind(current_file)
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(2, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()
