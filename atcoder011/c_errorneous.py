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

stack = [[first]]

success = False
while not success and len(stack) > 0:
    new_stack = []
    while len(stack) > 0:
        cur = stack.pop()
#        print cur, diff[cur[-1]]
        
        if cur[-1] == last:
            success = True
            break
        
        next = diff[cur[-1]]
        
        temp = []
        for n in next:
            if n not in cur:
                temp.append(n)
        
    #    temp.sort(key = lambda x: P[x], reverse=True)
        for t in temp:
            new_stack.append(cur + [t])
#    print stack, new_stack
    stack = new_stack
    stack.sort(key = lambda x: P[x[-1]], reverse=True)


if success:
    print len(cur) - 2
    print '\n'.join(cur)
else:
    print -1

#残り文字数ベースのA*？に書き換えようと思ったけど時間足らず……
