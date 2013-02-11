# -*- coding: utf-8 -*-
import math
import sys
import collections

stage = []
for line in sys.stdin:
    stage.append(line.strip())

count_x = 0
count_o = 0

S = len(stage)
L = len(stage[0])

check = [[0 for i in xrange(L)] for j in xrange(S)]

for i, s in enumerate(stage):
    for j, c in enumerate(s):
        if c == 'x':
            count_x += 1
            check[i][j] = -1
        elif c == 'o':
            count_o += 1
            check[i][j] = 1

win_o = False
win_x = False

check_yoko = [[0 for i in xrange(L)] for j in xrange(S)]
check_tate = [[0 for i in xrange(L)] for j in xrange(S)]
check_mnaname = [[0 for i in xrange(L)] for j in xrange(S)]
check_hnaname = [[0 for i in xrange(L)] for j in xrange(S)]
if count_o >= count_x and count_o - count_x < 2:
    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                for k in xrange(j, L):
                    if cur != check[i][k]:
                        break
                    else:
                        count += 1
                if count >= 10:
                    print 'NO'
                    sys.exit(0)
                elif 5 <= count <= 9:
                    for k in xrange(j, j + count):
                        check_yoko[i][k] = 1
                    if cur == -1:
                        win_x = True
                    else:
                        win_o = True
    
    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                for k in xrange(i, S):
                    if cur != check[k][j]:
                        break
                    else:
                        count += 1
                if count >= 10:
                    print 'NO'
                    sys.exit(0)
                elif 5 <= count <= 9:
                    for k in xrange(i, i + count):
                        check_tate[k][j] = 1
                    if cur == -1:
                        win_x = True
                    else:
                        win_o = True
    
    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                for k in xrange(min(S - i, L - j)):
                    if cur != check[i + k][j + k]:
                        break
                    else:
                        count += 1
                if count >= 10:
                    print 'NO'
                    sys.exit(0)
                elif 5 <= count <= 9:
                    for k in xrange(count):
                        check_mnaname[i][j] = 1
                    if cur == -1:
                        win_x = True
                    else:
                        win_o = True

    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                for k in xrange(min(i + 1, L - j)):
                    if cur != check[i - k][j + k]:
                        break
                    else:
                        count += 1
                if count >= 10:
                    print 'NO'
                    sys.exit(0)
                elif 5 <= count <= 9:
                    for k in xrange(count):
                        check_hnaname[i][j] = 1
                    if cur == -1:
                        win_x = True
                    else:
                        win_o = True
    
    test = 0
    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                count_check = 0
                for k in xrange(j, L):
                    if cur != check[i][k]:
                        break
                    else:
                        count += 1
                        if check_tate[i][k] == 1 or check_mnaname[i][k] == 1 or check_hnaname[i][k] == 1:
                            count_check += 1
                if 5 <= count <= 9:
                    if count_check >= 2:
                        print 'NO'
                        sys.exit(0)
                    elif count_check == 0:
                        test += 1
    
    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                count_check = 0
                for k in xrange(i, S):
                    if cur != check[k][j]:
                        break
                    else:
                        count += 1
                        if check_yoko[k][j] == 1 or check_mnaname[k][j] == 1 or check_hnaname[k][j] == 1:
                            count_check += 1 
                if 5 <= count <= 9:
                    if count_check >= 2:
                        print 'NO'
                        sys.exit(0)
                    elif count_check == 0:
                        test += 1
    
    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                for k in xrange(min(S - i, L - j)):
                    if cur != check[i + k][j + k]:
                        break
                    else:
                        count += 1
                        if check_yoko[i + k][j + k] == 1 or check_tate[i + k][j + k] == 1 or check_hnaname[i + k][j + k] == 1:
                            count_check += 1 
                if 5 <= count <= 9:
                    if count_check >= 2:
                        print 'NO'
                        sys.exit(0)
                    elif count_check == 0:
                        test += 1
    
    for i in xrange(S):
        for j in xrange(L):
            if abs(check[i][j]) == 1:
                cur = check[i][j]
                count = 0
                for k in xrange(min(i + 1, L - j)):
                    if cur != check[i - k][j + k]:
                        break
                    else:
                        count += 1
                        if check_yoko[i - k][j + k] == 1 or check_tate[i - k][j + k] == 1 or check_mnaname[i - k][j + k] == 1:
                            count_check += 1 
                if 5 <= count <= 9:
                    if count_check >= 2:
                        print 'NO'
                        sys.exit(0)
                    elif count_check == 0:
                        test += 1
    
    if test > 1:
        print 'NO'
        sys.exit(0)
    
    if win_o and win_x:
        print 'NO'
    elif not win_o and not win_x:
        print 'YES'
    elif win_o:
        if count_o > count_x:
            print 'YES'
        else:
            print 'NO'
    elif win_x:
        if count_o == count_x:
            print 'YES'
        else:
            print 'NO'
else:
    print 'NO'

#交差のチェックの時に、チェック済みの分を移動するのを忘れていたので、同じ列を何回もチェックしてしまっている(´・ω・｀)
