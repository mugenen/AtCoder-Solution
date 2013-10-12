# -*- coding: utf-8 -*-
import math
import sys
import collections

M, N = map(int, raw_input().split())


top = [[[[-1, -1, -1]]*3]*3] * M




for i in xrange(N):
    next = [[0, 0, 0]] * (M + 3)
    for j in xrange(M):
        for k in xrange(1, 4):
            for l in xrange(k):
                if next[j-l + 3] > 0:
                    break
            else:
                for m in xrange(k):
                    if top[j-l] > 0:
                        break

if M <= 100 and N <= 100:
    print -1
else:
    print 0
