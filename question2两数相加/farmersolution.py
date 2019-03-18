# !/usr/bin/python
# -*- coding:utf-8 -*-



class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 取出后相加并作类型转换
        num = str(self.init_ListNode(l1) + self.init_ListNode(l2))
        value_list = list(num)  #
        contains = []
        while value_list:  # 实例化所有的ListNode，并且让存入列表中
            val = value_list.pop()
            Node = ListNode(val)
            contains.append(Node)

        for n,i in enumerate(contains):  # 迭代并选择ListNode的list
            try:
                i.next = contains[n+1]
            except:
                pass

        return contains[0] 


    def init_ListNode(self, l:ListNode):
        """反转链表并返回值
        输入：(2 -> 4 -> 3)
        返回： '342' """

        curr = l
        head = None
        num = ''
        while curr:
            nextTemp = curr.next
            curr.next = head
            head = curr
            num = str(head.val) + num
            curr = nextTemp
        return int(num)

if __name__ == '__main__':

    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    test = Solution()
    c = test.addTwoNumbers(a,b)
    print(c.next.next.val)

