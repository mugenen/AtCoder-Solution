# -*- coding: utf-8 -*-
import math
import sys
import collections

n, m, Y, Z = map(int, raw_input().split())
weight = {}
block = ''
for line in sys.stdin:
    l = line.split()
    if len(l) == 2:
        c, p = l
        weight[c] = int(p)
    else:
        block = line.strip()

check = collections.Counter()
for c in block:
    check[c] += 1

def eval(b):
    score = 0
    if len(set(list(b))) == m:
        score += Z
    cur = ''
    count = 0
    for c in b:
        score += weight[c]
        if cur != c:
            if count != 0:
                score += count * Y
            count = 0
            cur = c
        else:
            count += 1
    else:
        if count != 0:
            score += count * Y
    return score

cand = []

cand.append(eval(block))
for d in check.most_common():
    cand.append(eval(d[0] * d[1]))

start = 0
end = 0
L = len(block)
cand_string = [block]
while len(cand_string) > 0:
    t_string = []
#    print cand_string
    for block in cand_string:
        while start < L :
            while end < L and block[start] == block[end]:
    #            print start, end
                end += 1
            new = block[:start] + block[end:]
            z = eval(new)
            if z > cand[-1]:
                cand.append(z)
                t_string.append(new)
            start = end
            cand.sort()
            cand.reverse()
            cand = cand[:1000]
    cand_string = t_string
cand.sort()
cand.reverse()
print cand[0]

#諦めた
#方針としては全部積んだ状態から、上位n件を残してビームサーチ
#比較対象としてすべて1色の場合も追加しておく
