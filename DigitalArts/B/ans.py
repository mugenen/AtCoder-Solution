import sys
import re

pwd = sys.stdin.readline().strip()

def toChar(n):
    if n == 0:
        return ''
    return chr(n - 1 + ord('a'))

def toHash(n):
    return ord(n) - ord('a') + 1

length = len(pwd)
if pwd != pwd[::-1]:
    print pwd[::-1]
elif len(pwd) == 1:
    if pwd != 'a':
        print 'a' + toChar(toHash(pwd) - 1)
    else:
        print 'NO'
elif len(pwd) == 20:
    if pwd == 'zzzzzzzzzzzzzzzzzzzz':
        print 'NO'
    elif pwd == 'aaaaaaaaaaaaaaaaaaaa':
        print 'aaaaaaaaaaaaaaaaaab'
    elif pwd != 'zzzzzzzzzzzzzzzzzzzz':
        for i in xrange(length):
            if pwd[i] != 'a':
                start = i
                for j in xrange(length):
                    if i == j:
                        continue
                    if pwd[j] != 'z':
                        end = j
        temp = list(pwd)
        temp[start] = toChar(toHash(pwd[start]) - 1)
        temp[end] =  toChar(toHash(pwd[end]) + 1)
        print ''.join(temp)
else:
    s = 0
    for c in pwd:
        s += toHash(c)
    for i in xrange(length):
        start = i
        temp = list(pwd)
        temp[start] = toChar(toHash(pwd[start]) - 1)
        cand = ''.join(temp)
        suc = False
        for j in xrange(length):
            if j == start:
                continue
            in_temp = list(pwd)
            in_temp[start] = toChar(toHash(pwd[start]) - 1)
            if in_temp[j] != 'z':
                in_temp[j] = toChar(toHash(pwd[j]) + 1)
                if ''.join(in_temp) != pwd:
                    suc = True
                    print ''.join(in_temp)
                    break
        if suc:
            break
        if cand + 'a' != pwd:
            print cand + 'a'
            break
        if (cand + 'a')[::-1] != pwd:
            print (cand + 'a')[::-1]
            break
        if 'a' + cand != pwd:
            print 'a' + cand
            break
        if ('a' + cand)[::-1] != pwd:
            print ('a' + cand)[::-1]
            break
    #list[end] =  toChar(toHash(pwd[end]) + 1)
    #print ''.join(temp)
