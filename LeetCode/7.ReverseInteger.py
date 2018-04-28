# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:16:08 2018

@author: sun
"""
#x = 123
#s = cmp(x,0) # positive, zero or negative
#num_rev = int(str(s*x)[::-1]) # reverse the number part
#over = num_rev < 2**31
#new = s*num_rev*over
#print s
#print int(num_rev)
#print over
#print new

X = 12321
x = X
new = 0
D = 0
while x != 0:
    I = x/10
    D = x%10
    new = D + new * 10
    x = x/10

if new == X:
    print 1
else:
    print 0