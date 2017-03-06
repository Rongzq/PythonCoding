# -*- coding: utf-8 -*-
"""
@Author  : Rongzq (jerry.rongzq@outlook.com)
@Link    : https://github.com/Rongzq/PythonCoding
@Date    : 2017/3/6 11:34
@Version : 0.1
@History : exercise of HWPython, while-loop


"""

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")
for num in numbers:
    print(num)
