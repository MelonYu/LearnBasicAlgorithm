#!/usr/bin/env python

# -*- encoding: utf-8 -*-

"""
@Author  :   Amelia 
@Contact :   yu_mengling@hust.edu.cn
@File    :   5. Longest Palindromic Substring.py
 
@Time    :   18-6-5 下午9:48
"""


class Solution:

    def expandAroundCenter(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
        return r - l - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 找到回文串的中心：可能是一个字母比如aba中的b，可能是一个空比如bb的中间
        # 从中间向两边延伸，看其是否是一个回文串
        # 第一种情况(aba)时,中心有n个，第二种(bb)时，中心应该n-1个，所以一共有2n-1个

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)  # 第一种情况
            len2 = self.expandAroundCenter(s, i, i + 1)  # 第二种情况
            ans = max(len1, len2)
            # 当找到的回文串长度比当前的子串长度大时，重新设定最大回文串的起始位置和结束位置
            if ans > (end - start):
                start = i - (ans - 1) // 2
                end = i + ans // 2

        return s[start:end + 1]


if __name__ == '__main__':
    sol = Solution()
    test_case = ['babad', 'abba']
    for s in test_case:
        print('%s: %s' % (s, sol.longestPalindrome(s)))  # The answer is aba
