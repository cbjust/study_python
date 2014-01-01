#!/usr/env/python
# Author: Justin Chen
# Date: 2014.1.1

class TestIter:
    '''print list from iter'''
    def __init__(self):
        self.value = 0
    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

#help(TestIter)
ti = TestIter()
print list(ti)
