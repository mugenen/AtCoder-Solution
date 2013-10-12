# -*- coding: utf-8 -*-

N = int(raw_input())

T = []

for i in xrange(N):
    s, e = raw_input().split()
#    s = int("".join(s.split(':')))
#    e = int("".join(e.split(':')))
    sh, sm = s.split(':')
    s = 60 * int(sh) + int(sm)
    eh, em = e.split(':')
    e = 60 * int(eh) + int(em)
    T.append((s, e))

T.sort(key = lambda x: x[0])


c = 0
while len(T) > 0:
    c += 1
    t = T.pop(0)
    h = t
    i = 0
    while i < len(T):
        if t[1] <= T[i][0] and T[i][1] - 24 * 60 <= h[0]:
            t = T.pop(i)
            i -= 1
        i += 1

print c
