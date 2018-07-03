#!/usr/bin/env python

# -*- encoding: utf-8 -*-

"""
@Author  :   Amelia 
@Contact :   yu_mengling@hust.edu.cn
@File    :   17. Letter Combinations of a Phone Number.py
 
@Time    :   18-7-3 下午8:31
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_str = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # 每个数字有各自对应的几种选择，最后的结果是其中的一种拼接起来
        if not digits:
            return []
        digits = list(map(int, digits))
        ans = ['']
        for d in digits:
            if d <= 1:
                continue
            ans = [a + s for a in ans for s in digits_str[d]]

        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.letterCombinations('23')
    print(ans)

