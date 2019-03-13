# !/usr/bin/python
# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            NextTemp = curr.next
            curr.next = pre
            pre = curr
            curr = NextTemp
        return pre

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c

    print(a.val)
    print(a.next.val)
    print(a.next.next.val)

    test = Solution()
    #
    result = test.reverseList(a)
    print(result.val)
    print(result.next.val)
    print(result.next.next.val)