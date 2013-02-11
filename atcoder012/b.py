# -*- coding: utf-8 -*-
import math
import sys
import datetime

N, va, vb, L = map(int, raw_input().split())

d = float(L)
for i in xrange(N):
    t = d / va
    d = vb * t
print '{:.10f}'.format(d)
