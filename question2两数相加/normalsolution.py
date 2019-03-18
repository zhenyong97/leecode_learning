class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        add = 0
        l3 = ListNode(0)
        node = l3
        while l1 or l2:
            cur = ListNode(add)
            if l1:
                cur.val += l1.val
                l1 = l1.next
            if l2:
                cur.val += l2.val
                l2 = l2.next
            add = cur.val // 10
            cur.val = cur.val % 10
            node.next, node = cur, cur
        if add:
            node.next = ListNode(add)
        
        return l3.next
		
if __name__ == '__main__':

    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    test = Solution()
    c = test.addTwoNumbers(a,b)
    print(c.next.next.val)
