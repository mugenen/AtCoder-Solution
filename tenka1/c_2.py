# -*- coding: utf-8 -*-
import itertools

N = int(raw_input())

T = []

for i in xrange(N):
    s, e = raw_input().split()
    s = int("".join(s.split(':')))
    e = int("".join(e.split(':')))
    T.append((s, e))

c = 100
for p in itertools.permutations(T):
    i = 1
    t = p[0]
    cc = 1
    while i < len(p):
#        print t, p[i], 'XXX'
        if p[i][0] >= t[1] and (p[i][1] - 2400 <= t[0]):
            pass
        else:
#            print t, p[i], 'change'
            t = p[i]
            cc += 1
        i += 1
    c = min(c, cc)

print c
