# -*- coding=utf-8 -*-

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: listNode
        :type l2: listNode
        :rtype: ListNode
        """
        # 进位数
        carry = 0
        
        # 初始化结果链表的头结点
        # root 用于指向结果的头结点，便于返回值
        root = n = ListNode(0)
        
        # 当l1，l2有一个链表不为空，或进位数不为0时
        while l1 or l2 or carry:
            v1 = v2 = 0 
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
                
            # 得到进位数和个位数
            carry, v = divmod(carry+v1+v2, 10)
            # 将个位数加入结果链表，进位数参与下次循环
            n.next = ListNode(v)
            n = n.next
            
        return root.next
