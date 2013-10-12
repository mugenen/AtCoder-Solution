# -*- coding: utf-8 -*-
import math
import sys
import datetime

N = int(raw_input())

result = 0
for i in xrange(N):
    line = raw_input()
    if sum(map(int, line.split())) < 20:
        result += 1
print result
