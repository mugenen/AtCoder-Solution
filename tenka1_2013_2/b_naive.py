# -*- coding: utf-8 -*-
import math
import sys
import datetime

Q, L = map(int, raw_input().split())

stack = []

if Q > 50 or N > 50:
    print ''
    sys.exit()

for i in xrange(Q):
#    print stack, len(stack)
    line = raw_input()
    query = line.split()
    l = len(query)
    if l == 1:
        if query[0] == 'Top':
            if len(stack) > 0:
                print stack[-1]
            else:
                print 'EMPTY'
                break
        elif query[0] == 'Size':
            print len(stack)
    elif l == 2:
        sub = int(query[1])
        while len(stack) > 0 and sub > 0:
            stack.pop()
            sub -= 1
        
        if sub > 0:
            if count == len(stack):
                print 'EMPTY'
                break
    elif l == 3:
        add = int(query[1])
        num = int(query[2])
        if len(stack) + add > L:
            print 'FULL'
            break
        else:
            for q in xrange(add):
                stack.append(num)
else:
    print 'SAFE'

#print stack, size
