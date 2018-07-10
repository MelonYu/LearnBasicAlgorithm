#!/usr/bin/env python

# -*- encoding: utf-8 -*-

"""
@Author  :   Amelia 
@Contact :   yu_mengling@hust.edu.cn
@File    :   19. Remove Nth Node From End of List.py
 
@Time    :   18-7-3 下午9:29
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    pass