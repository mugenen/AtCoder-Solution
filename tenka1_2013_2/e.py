# -*- coding: utf-8 -*-
import math
import sys
import collections

last = (4, 6)
for i in xrange(1):
    print 0 + last[0], 0 + last[1]
    print -3 + last[0], 0 + last[1]
    print -3 + last[0], -4 + last[1]
    print -2 + last[0], -1 + last[1]
    last = (2 + last[0], 4 + last[1])
