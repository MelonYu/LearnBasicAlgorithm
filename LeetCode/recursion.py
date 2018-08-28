#!/usr/bin/env python

# -*- encoding: utf-8 -*-

"""
@Author  :   Amelia 
@Contact :   yu_mengling@hust.edu.cn
@File    :   recursion.py
 
@Time    :   18-8-28 22:05
"""

import time


def performance(f):
    def fn(*args, **kw):
        t_start = time.time()
        r = f(*args, **kw)
        t_end = time.time()
        print('call %s(%s) in %fs' % (f.__name__, args[1:], (t_end - t_start)))
        return r

    return fn


class Factorial(object):

    # 递归的方法
    @performance
    def f_rec(self, n):
        if n == 1:
            return 1
        else:
            return n * self.f_rec(n-1)

    # 循环
    @performance
    def f_loop(self, n):
        ans = 1
        while n >= 1:
            ans = ans * n
            n = n - 1
        return ans


class Fib(object):

    @performance
    def fib_rec(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib_rec(n-1) + self.fib_rec(n - 2)

    @performance
    def fib_rec_opt(self, first, second, n):
        if n > 0:
            if n == 1:
                return first
            elif n == 2:
                return second
            elif n == 3:
                return first + second

            return self.fib_rec_opt(second, first+second, n - 1)
        return -1


if __name__ == '__main__':
    # fac = Factorial()
    # print(fac.f_rec(4))
    # print(fac.f_loop(4))
    fib = Fib()
    print(fib.fib_rec(6))
    print(fib.fib_rec_opt(1, 1, 6))
