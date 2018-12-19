# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        i=0
        tp=head
        cur=head
        prev=None
        
        while(cur and i<k):
            cur=cur.next
            i+=1
        if i!=k:
            return tp
        cur=tp
        i=0
        while cur and i<k:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
            i+=1
        
        head.next = self.reverseKGroup(cur,k)
        return prev
