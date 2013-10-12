# -*- coding: utf-8 -*-
import sys
import collections

text = []
for line in sys.stdin:
    text.append(line.strip())
text.sort()

print text[6]
