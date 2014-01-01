#!/usr/bin/python
# Author: Justin Chen
# Date: 2014.01.01

#Note: add fibonacci func

class Fibs:
    '''print Fibonacci number less than 1000'''
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

print Fibs.__doc__
fibs = Fibs()
print 0,
for f in fibs:
    if f > 1000:
        break
    print f,
