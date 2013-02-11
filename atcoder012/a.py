# -*- coding: utf-8 -*-
import sys
import collections

day = raw_input().strip()

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


i = days.index(day)
if i > 1:
    print (7 - days.index(day)) % 7
else:
    print 0
