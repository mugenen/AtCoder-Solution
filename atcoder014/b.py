# -*- coding: utf-8 -*-
import math
import sys
import datetime

N = int(raw_input())

check = set()

result = ['LOSE', 'WIN']

before = ''
for i in xrange(N):
    line = raw_input()
    if line in check:
        print result[i % 2]
        break
    check.add(line)
    if i > 0 and before[-1] != line[0]:
        print result[i % 2]
        break
    before = line
else:
    print 'DRAW'
