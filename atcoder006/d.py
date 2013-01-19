# -*- coding: utf-8 -*-
import math
import collections

H, W = map(int, raw_input().split())


A = collections.OrderedDict()
#A[(0, 0)] = True
A[(-1, 1)] = True
A[(1, 1)] = True
A[(-2, 2)] = True
A[(2, 2)] = True
A[(-2, 3)] = True
A[(-1, 3)] = True
A[(0, 3)] = True
A[(1, 3)] = True
A[(2, 3)] = True
A[(-2, 4)] = True
A[(2, 4)] = True

point = collections.OrderedDict()
for i in xrange(H):
    inner = raw_input()
    for j in xrange(W):
        if inner[j] == 'o':
            point[(i, j)] = True


def isA(p):
    rate = 1
    length = 1
    cur = p[0] + 1
    while (cur, p[1]) in point:
        length += 1
        cur += 1
    
    #ã‚ÌŒü‚«
    count = 0
    for a in A:
        if (p[0] + a[0], p[1] + a[1]) in point:
            count += 1
            print "match", (p[0] + a[0], p[1] + a[1]), p
    print count, p
    #‰ºŒü‚«
    #if length % 3 == 0:#‰¡Œü‚«
        

for p in point:
    isA(p)

print point
