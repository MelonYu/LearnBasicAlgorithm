#!/usr/bin/env python

# -*- encoding: utf-8 -*-

"""
@Author  :   Amelia 
@Contact :   yu_mengling@hust.edu.cn
@File    :   22_generate_parentheses.py
 
@Time    :   18-8-28 下午9:27
"""


class Solution:

    def generateParenthesis(self, N):
        """
        :type N: int
        :rtype: List[str]
        """
        # 排列组合，其中只有部分是有效的结果

        # 记录左括号和右括号的数量，当左括号比右括号多的时候，可以再加左括号或者右括号，
        # 直到左括号数量为N时则只能加右括号
        # 直到总长度为2N时，生成完毕
        ans = []

        def backtrack(S='', left=0, right=0):
            print(S, left, right)
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                # print(left, right)
                backtrack(S + '(', left + 1, right)
            if right < left:
                # print(left, right)
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 3
    a = sol.generateParenthesis(n)
    print(a)
