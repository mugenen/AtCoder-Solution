# -*- coding: utf-8 -*-
import sys
import collections
m, n, N = map(int, raw_input().split())

consumed = N

sold = N
while consumed >= m:
    consumed -= m
    consumed += n
    sold += n

print sold
