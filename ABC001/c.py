# -*- coding: utf-8 -*-
import math
import sys
import datetime

deg, dis = map(int, raw_input().split())

direction = 'N'
seed_d = [11.25, 33.75, 56.25, 78.75, 101.25, 123.75, 146.25, 168.75, 191.25, 213.75, 236.25, 258.75, 281.25, 303.75, 326.25, 348.75]
cond_d = [(seed_d[i], seed_d[i + 1]) for i in xrange(len(seed_d) - 1)]
name_d ='NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW'.split(' ')

for i, k in enumerate(cond_d):
    l, u = k
    if l <= deg / 10.0 + 0.000001 < u:
        direction = name_d[i]

seed_p = [0.0, 0.3, 1.6, 3.4, 5.5, 8.0, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7]
cond_p = [(seed_p[i], round(seed_p[i + 1] - 0.1, 1)) for i in xrange(len(seed_p) - 1)]

power = 12
for i, k in enumerate(cond_p):
    l, u = k
    if l <= round(dis / 60.0 + 0.000001, 1) <= u:
        power = i

if power == 0:
    print 'C', 0
else:
    print direction, power
#print deg, dis
#print deg / 10.0, round(dis / 60.0 + 0.000001, 1)
