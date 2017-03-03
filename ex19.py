# -*- coding: utf-8 -*-
# @Date    : 2017-03-03 08:57:14
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 19 of HWPython, 函数和变量

import os

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print ("You have %d cheese!\n" % cheese_count)
	print ("You have %d boxes of crackers\n" % boxes_of_crackers)
	print ("Man that's enough for a party!")
	print ("Get a blanket.\n")

print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crakers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crakers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print ("And we can combine two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crakers+1000)


