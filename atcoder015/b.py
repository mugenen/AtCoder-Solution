# -*- coding: utf-8 -*-
import math
import sys
import datetime

N = int(raw_input())
result = [0] * 6

for i in xrange(N):
    M, m = map(float, raw_input().split())
    if 35 <= M:
        result[0] += 1
    if 30 <= M < 35:
        result[1] += 1
    if 25 <= M < 30:
        result[2] += 1
    if 25 <= m:
        result[3] += 1
    if m < 0 and 0 <= M:
        result[4] += 1
    if M < 0:
        result[5] += 1

for i in result:
    print i,

