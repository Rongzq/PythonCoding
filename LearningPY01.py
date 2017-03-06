# -*- coding: utf-8 -*-
"""
@Author  : Rongzq (jerry.rongzq@outlook.com)
@Link    : https://github.com/Rongzq/PythonCoding
@Date    : 2017/3/6 17:17
@Version :
@History : list 和 tuple; 条件判断


"""

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

#打印Apple:
print(L[0][0])

#打印Python
print(L[1][1])

#打印Lisa
print(L[2][2])

height = 1.75
weight = 80.5

BMI = weight / (height * height)
if BMI <= 18.5:
    print("过轻")
elif BMI >= 18.5 and BMI <= 25:
    print("正常")
elif BMI >=25 and BMI <= 28:
    print("过重")
elif BMI >=28 and BMI <= 32:
    print("肥胖")
else:
    print('严重肥胖')