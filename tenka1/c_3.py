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
    T.append([s, e, False])

T.sort(key = lambda x: x[0])

c = 0
for q in T:
    if q[2]:
        continue
    c += 1
    t = []
    t.append(q)
    q[2] = True
    for p in T:
        if p[2]:
            continue
        def overwrap(S, y):
            for x in S:
                if x[0] < y[0] < x[1] or x[0] < y[1] < x[1] or x[0] < y[0] - 1440 < x[1] or x[0] < y[1] - 1440 < x[1] or x[0] < y[0] + 1440 < x[1] or x[0] < y[1] + 1440 < x[1]:
                    return True
            return False
        
        if not overwrap(t, p):
            t.append(p)
            p[2] = True
            i -= 1
        i += 1

print c

