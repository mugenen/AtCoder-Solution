# -*- coding: utf-8 -*-
import math
import sys
import collections


all, N, M = map(int, raw_input().split())

L = []
for i in xrange(N):
    L.append(int(raw_input()))

xy = []
for i in xrange(M):
    xy.append(map(int, raw_input().split()))

diff = []

for i in xrange(N - 1):
    diff.append(L[i + 1] - L[i])

for A, B in xy:
    count = 0
    start = L[0]
    end = L[0]

#    if start - A <= 0:
#        count -= 1 - (start - A)
#    print 'start', count
    for i in xrange(N - 1):
        if diff[i] <= A + B:
            end = L[i + 1]
        else:
            count += min(end + B, all) - max(1, start - A) + 1
#            print count, end, start, A, B, max(1, start - A), min(end + B, all)
            start = L[i + 1]
            end = L[i + 1]
#            if i + 2 < N:
#                start = L[i + 2]
#                end = L[i + 2]
    count += min(end + B, all) - max(1, start - A) + 1
#    print count, end, start, A, B, max(1, start - A), min(end + B, all)

    print count
