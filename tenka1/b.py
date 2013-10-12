# -*- coding: utf-8 -*-
a = list(raw_input())

i = 0

L = len(a)

head = 0
tail = L
for i in xrange(L):
    if a[i] == '_':
        head += 1
    else:
        break

for j in xrange(L - 1, -1, -1):
#    print i, len(a), a[13], a[14], a[15]
    if a[j] == '_':
        tail -= 1
    else:
        break



def isSnake(a, head, tail):
    S = a[head:tail]
    
    check = 0
    for i in S:
        if i == '_':
            check += 1
            if check >= 2:
                return False
        else:
            check = 0
    
    for i in "".join(S).split('_'):
        F = True
        for j in i:
            if not('0' <= j <= '9') and not('a' <= j <= 'z'):
                return False
            if '0' <= j <= '9' and F:
                return False
            F= False
    return True

def snakeToCamel(a, head, tail):
    i = 0
    while head <= i < tail:
#    print i, a[i] == '_'
        if a[i] == '_':
            a[i + 1] = a[i + 1].upper()
            a.pop(i)
            i -= 1
            tail -= 1
        i += 1
    print "".join(a)

def isCamel(a, head, tail):
    S = a[head:tail]

    check = 0
    for i in S:
        if 'A' <= i <= 'Z':
            check += 1
            if check >= 2:
                return False
        else:
            check = 0

    if '0' <= S[0] <= '9' or 'A' <= S[0] <= 'Z':
        return False
    for i in S:
        if not('0' <= i <= '9') and not('a' <= i <= 'z') and not('A' <= i <= 'Z'):
            return False
#    print 'Camel'
    return True

def camelToSnake(a, head, tail):
    i = head
    while head <= i < tail:
        if 'A' <= a[i] <= 'Z':
            a[i] = a[i].lower()
            a.insert(i, '_')
            tail -= 1
            i += 1
        i += 1
    print "".join(a)

if isSnake(a, head, tail):
    snakeToCamel(a, head, tail)
elif isCamel(a, head, tail):
    camelToSnake(a, head, tail)
else:
    print "".join(a)
