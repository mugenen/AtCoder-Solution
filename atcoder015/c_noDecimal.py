# -*- coding: utf-8 -*-
import math
import sys
import collections

N = int(raw_input())


route = collections.defaultdict(set)

large = [1]
small = [1]


for i in xrange(N):
    l, n, r = raw_input().split()
    n = int(n)
    route[l].add((r, 1, n))
    route[r].add((l, n, 1))

def search(current, visited, cur_m, cur_d):
#    print current, cur_m, cur_d
    for next, m, d in route[current]:
        if next not in visited:
            visited.add(next)
            score = cur_m / cur_d
            score *= m
            score /= d
            if score > large[0]:
                large[0] = score
                largest[0] = next
            if score < small[0]:
                small[0] = score
                smallest[0] = next
            search(next, visited, cur_m * m, cur_d * d)
#            visited.remove(next)

first = route.keys()[0]
largest = [first]
smallest = [first]

search(first, set([first]), 1.0, 1.0)

#print large, small, int(round(large[0] / small[0]))
print '1{}={}{}'.format(largest[0], int(round(large[0] / small[0])), smallest[0])
