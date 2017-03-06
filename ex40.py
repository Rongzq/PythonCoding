# -*- coding: utf-8 -*-
"""
@Author  : Rongzq (jerry.rongzq@outlook.com)
@Link    : https://github.com/Rongzq/PythonCoding
@Date    : 2017/3/6 14:51
@Version :
@History : 字典练习


"""

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"

cities['_find'] = find_city
# 函数同样可以做变量, 将函数'find_city' 放在叫做'cities'的字典中, 并标记为'_find'

while True:
    print("State? (Enter to quite"),
    state = input("> ")

    if not state: break

    city_found = cities['_find'](cities, state)
    print(city_found)
