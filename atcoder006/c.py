# -*- coding: utf-8 -*-
import math


N = int(raw_input())

w = int(raw_input())
stack = [[w]]
for i in xrange(N - 1):
    w = int(raw_input())
    for j in stack:
        if j[-1] >= w:
            j.append(w)
            break
    else:
        stack.append([w])
    stack.sort(lambda x, y: cmp(x[-1], y[-1]))
#    print stack



print len(stack)
