# -*- coding: utf-8 -*-
# @Date    : 2017-02-24 14:51:33
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 04 of HWPython

import os

cars = 100
speac_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * speac_in_a_car
average_passengers_per_car = passengers / cars_driven

print ('there are', cars, 'cars available')
print ('There are only', drivers, 'drivers available.')
print ('There will be', cars_not_driven, 'empty cars today')
print ('We can transport', carpool_capacity, 'people today')
print ('We have', passengers, 'to carpool today.')
print ('We need to put about', average_passengers_per_car, 'in each cars_driven.')
