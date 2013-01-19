# -*- coding: utf-8 -*-
import math


N, L = map(int, raw_input().split())

root = []
for i in xrange(L):
    line = raw_input()
    cross = set()
    for j in xrange(len(line)):
        if line[j] == '-':
            cross.add(j)
    root.append(cross)
line = raw_input()

start = 0
for i in xrange(len(line)):
    if line[i] == 'o':
        start = i
        break
        
root.reverse()

#print start, root
for i in root:
#    print start, i
    if start + 1 in i:
        start += 2
    elif start - 1 in i:
        start -= 2

print int(math.floor(start / 2.0) + 1)
