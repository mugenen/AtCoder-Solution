# -*- coding: utf-8 -*-
import math
import sys
import datetime

N = int(raw_input())

l = set()
for line in sys.stdin:
    m, d = map(int, line.split('/'))
    t = int(datetime.date(2012, m, d).strftime('%j'))
    while t <= 366:
        if t not in l:
            l.add(t)
            break
        t += 1

for i in xrange(1, 13):
    for j in xrange(1, 32):
        try:
            w = datetime.date(2012, i, j).weekday()
            if w >= 5:
                t = int(datetime.date(2012, i, j).strftime('%j'))
                while t <= 366:
                    if t not in l:
                        l.add(t)
                        break
                    t += 1
        except:
            pass
l = list(l)
l.sort()

m = 0
count = 0
cur = 0
for i in l:
    if int(i) == cur + 1:
        cur = int(i)
        count += 1
    else:
        cur = int(i)
        count = 1
    if count > m:
        m = count
print m
