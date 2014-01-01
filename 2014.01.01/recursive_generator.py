#!/usr/env/python
#coding:utf-8
# Author: Justin Chen
# Date: 2014.1.1

#Note: zh-rCN: 递归生成器，解析多层嵌套

def flatten(nested):
    '''Parsing nested: recursion with using yield'''
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

#help(flatten)

#start test---------------------------------------

nested_one = [[1,2],[3,4],[5], 6, 7]
nested_two = [[[1],2],3,4,[5, [6, 7]], 8]

print list(flatten(nested_one))
print list(flatten(nested_two))
