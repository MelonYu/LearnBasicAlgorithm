# -*- coding: utf-8 -*-
"""
Created on Wed May 02 10:26:01 2018

@author: sun
"""


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    slist = map(str,s)
    sym_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sign = [1]*len(slist)
    for i in range(len(slist)-1):
        print sym_val[slist[i]]
        x = sym_val[slist[i+1]] / sym_val[slist[i]]
        if x == 5 or x == 10:
            sign[i] = -1
    print sign
    result = 0
    for j in range(len(slist)):
        result += sign[j] * sym_val[slist[j]]
        print result
    return result

romanToInt('MCMXCIV') 