# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 21:06:42 2018

@author: sun
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    sumlist = ListNode()
    while l1.next != None or l2.next != None:
        apd = 0
        s = l1.val + l2.val + apd
        apd = s/10
        s = s%10
        sumlist.val = s
        
        l1 = l1.next
        l2 = l2.next
        print sumlist.val
        sumlist = sumlist.next
            
if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(5)
    addTwoNumbers(l1,l2)