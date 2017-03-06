# -*- coding: utf-8 -*-
"""
@Author  : Rongzq (jerry.rongzq@outlook.com)
@Link    : https://github.com/Rongzq/PythonCoding
@Date    : 2017/3/6 17:46
@Version :
@History : 循环


"""

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n = n -2
print(sum)

sum = 0
n = 1
while n < 100:
    sum += n
    n += 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello, %s!" % name)

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue # continue 语句会跳过下面的语句直接下一轮循环, 后续的print语句就不会执行
    print(n)
