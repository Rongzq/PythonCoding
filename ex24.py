# -*- coding: utf-8 -*-
# @Date    : 2017-03-03 09:07:18
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 24 of HWPython, 练习

print("Let's practice everything.")
print('You\'d need to know \'bout with  that do \n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------------")
print(poem)
print("-------------------")


five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point /= 10

print("We can also to that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
