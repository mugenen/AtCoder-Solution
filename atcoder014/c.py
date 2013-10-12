# -*- coding: utf-8 -*-
import math
import sys
import collections

deq = collections.deque()

N = int(raw_input())

ball = raw_input()

candidate = [(0, deq)]

for b in ball:
    new_candidate = []
    for n, d in candidate:
        L = len(d)
        if L == 0:
            d.append(b)
        else:
            head = d[0]
            tail = d[-1]
            if head == b:
                d.popleft()
            elif tail == b:
                d.pop()
            elif L == 1 or head == tail:
                d.append(b)
            else:
                d2 = collections.deque(d)
                d.append(b)
                d2.appendleft(b)
                new_candidate.append((len(d2), d2))
        new_candidate.append((len(d), d))
    new_candidate.sort()
#    print new_candidate
    candidate = new_candidate[:10000]

#print candidate
print candidate[0][0]
