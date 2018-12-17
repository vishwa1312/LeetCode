# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #TreeLinkNode tmp= root
        if root:
            q=[root,"#"]
        else:
            return None
        i=0
        while q:
            if q[i]=="#":
                q.append("#")
                if q[i]==q[i+1]:
                    break
                i+=1
                continue
            if q[i].left:
                q.append(q[i].left)
            if q[i].right:
                q.append(q[i].right)
            i+=1
        
        for i in xrange(len(q)):
            if q[i]=="#":
                continue
            if q[i+1]=="#":
                q[i].next=None
            else:
                q[i].next=q[i+1]
        
