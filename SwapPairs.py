# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        cur=head
        prev=None
        i=0
        while cur and i<2:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
            i+=1
        head.next=self.swapPairs(cur)
        return prev
