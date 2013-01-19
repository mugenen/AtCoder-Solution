# -*- coding: utf-8 -*-
import sys
N, M, A, B = map(int, raw_input().split())
i = 1
for line in sys.stdin:
    c = int(line)
    if N <= A:
        N += B
    N -= c
    if N < 0:
        print i
        break
    i += 1
else:
    print 'complete'
