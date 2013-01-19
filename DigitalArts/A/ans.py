import sys
import re

words = sys.stdin.readline().strip().split()
N = int(sys.stdin.readline().strip())

filter = []
for line in sys.stdin:
    filter.append(line.strip())

r = []
for f in filter:
    r.append(re.compile(f.replace('*', '.')))

for w in words:
    for m in r:
        result = m.match(w)
        length = len(w)
        if result != None and result.end() == length:
            print '*' * length,
            break
    else:
        print w,
