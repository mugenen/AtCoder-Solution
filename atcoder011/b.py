# -*- coding: utf-8 -*-
import math
import sys
import datetime

N = int(raw_input())
word = raw_input().split()

ret = []
check = [['z', 'r'], ['b', 'c'], ['d', 'w'], ['t', 'j'], ['f', 'q'], ['l', 'v'], ['s', 'x'], ['p', 'm'], ['h', 'k'], ['n', 'g']]
new_check = []
for q in check:
    temp = []
    for e in q:
        temp.append(e)
        temp.append(e.upper())
    new_check.append(temp)
check = new_check
for w in word:
    result = []
    for c in w:
        for i, q in enumerate(check):
            for e in q:
                if c == e:
#                    print c, e, i
                    result.append(str(i))
    if len(result) > 0:
        ret.append(''.join(result))

print ' '.join(ret)
