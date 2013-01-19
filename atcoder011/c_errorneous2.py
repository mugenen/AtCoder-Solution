# -*- coding: utf-8 -*-
import math
import sys
import collections

first, last = raw_input().strip().split()
N = int(raw_input())
word = []
for i in xrange(N):
    word.append(raw_input().strip())

if first == last:
    print 0
    print first
    print last
    
    sys.exit(0)

L = len(first)

diff = collections.defaultdict(set)

P = {}
for i in word + [first, last]:
    P[i] = sum([i[c] != last[c] for c in xrange(L)])

for i in word + [first, last]:
    for j in word + [first, last]:
        if sum([i[c] != j[c] for c in xrange(L)]) == 1:
            diff[i].add(j)
            diff[j].add(i)


distance = collections.defaultdict(lambda: 10000)

cur = [first]
distance[first] = -1

while len(cur) > 0:
    new_cur = []
    for c in cur:
        for next in diff[c]:
            if distance[next] > distance[c] + 1:
                distance[next] = distance[c] + 1
                new_cur.append(next)
    cur = new_cur

if distance[last] != 10000:
    print distance[last]
    
    cur = last
    route =[cur]
    while True:
        if cur == first:
            break
        for next in diff[cur]:
            if distance[next] == distance[cur] - 1:
                cur = next
                route.append(cur)
                break
    route.reverse()
    print '\n'.join(route)
else:
    print -1
#残り文字数ベースのA*？に書き換えようと思ったけど時間足らず……
