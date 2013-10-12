# -*- coding: utf-8 -*-
import math
import sys
import datetime

Q, L = map(int, raw_input().split())

stack = []
size = 0

for i in xrange(Q):
#    print stack, size
    line = raw_input()
    query = line.split()
    l = len(query)
    if l == 1:
        if query[0] == 'Top':
            if size > 0:
                print stack[-1][0]
            else:
                print 'EMPTY'
                break
        elif query[0] == 'Size':
            print size
    elif l == 2:
        sub = int(query[1])
        sub_org = sub
        count = 0
        
        for j in xrange(len(stack) - 1, -1, -1):
            if sub >= stack[j][1]:
                count += 1
                sub -= stack[j][1]
        if sub > 0:
            if count == len(stack):
                print 'EMPTY'
                break
            else:
                del stack[-count:]
                target = stack.pop()
                stack.append((target[0], target[1] - sub))
        else:
            del stack[-count:]
        size -= sub_org
    elif l == 3:
        add = int(query[1])
        num = int(query[2])
        if size + add > L:
            print 'FULL'
            break
        else:
            stack.append((num, add))
            size += add
else:
    print 'SAFE'

#print stack, size
