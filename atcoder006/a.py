# -*- coding: utf-8 -*-
correct = set(map(int, raw_input().split()))
bonus = int(raw_input())
given = set(map(int, raw_input().split()))

if len(correct & given) == 6:
    print 1
elif len(correct & given) == 5 and bonus in given:
    print 2
elif len(correct & given) == 5:
    print 3
elif len(correct & given) == 4:
    print 4
elif len(correct & given) == 3:
    print 5
else:
    print 0
