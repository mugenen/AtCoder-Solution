# -*- coding: utf-8 -*-
import sys
import collections

N = int(raw_input())

L = (100 * N) + 1
score = [0] * L

score[0] = 1

for p in map(int, raw_input().split()):
    for j in xrange(L - 1, -1, -1):
        if score[j] == 1 and j + p < L:
            score[j + p] = 1

print sum(score)
