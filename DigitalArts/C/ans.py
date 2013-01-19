import sys
import re
import collections

N, M, K = map(int, sys.stdin.readline().strip().split())

count = collections.Counter()
link = collections.defaultdict(set)

for i in xrange(1, N + 1):
    link[i].add(i)
for line in sys.stdin:
    l = line.strip()
    if l[0] == 't':
        a, b = l.split()
        b = int(b)
        for i in link[b]:
            count[i] += 1
#            print 'add', i
    elif l[0] == 'f':
        a, b, c = l.split()
        b = int(b)
        c = int(c)
        link[b].add(c)
        link[c].add(b)
#        print 'follow', b, c
    elif l[0] == 'u':
        a, b, c = l.split()
        b = int(b)
        c = int(c)
        link[b].remove(c)
        link[c].remove(b)
#        print 'unfollow', b, c

if len(count) < K:
    print 0
else:
    result = count.most_common()
    print result[K - 1][1]
