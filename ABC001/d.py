# -*- coding: utf-8 -*-
import math
import sys
import datetime

raw_input()

history = set()
for line in sys.stdin:
    start, end = line.strip().split('-')
    start = int(start[:2]) * 60 + int(start[2:])
    start = start / 5 * 5
    end = int(end[:2]) * 60 + int(end[2:])
    end = (end + 4) / 5 * 5
    history.add((start, end))
#    print start, end

raining = [0] * (2405 / 5)

for s, e in history:
    s = s / 5
    e = e / 5
    raining[s] += 1
    raining[e] -= 1

L = len(raining)
acc = 0
for i in xrange(L):
    if acc == 0 and raining[i] != 0:
        head = i * 5
    acc += raining[i]
    if acc == 0 and raining[i] != 0:
        print '{:04d}-{:04d}'.format(head / 60 * 100 + (head % 60), (i * 5) / 60 * 100 + ((i * 5) % 60))

