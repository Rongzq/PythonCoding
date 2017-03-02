# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 16:46:01
# @Author  : Rongzq (jerry.rongzq@outlook.com)
# @Link    : https://github.com/Rongzq/PythonCoding
# @Version : $Id$
# @History : exercise 17 of HWPython, 更多文件操作

from os.path import exists
from sys import argv

script, from_file, to_file = argv

print ("Copying form %s to %s" % (from_file, to_file))

#how to do these on one line?
input_file = open(from_file)
indata = input_file.read()

print ("The input file is %d bytes long" % len(indata))

print ("Does the output file exit? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output = open(to_file, 'w')
output.write(indata)

print ("Alright, all done")

output.close()
input_file.close()
