# -*- coding: utf-8 -*-
import sys
import collections

s = 42
for i in xrange(100):
    s *= 2
    if s > 130000000:
        print s
        break
