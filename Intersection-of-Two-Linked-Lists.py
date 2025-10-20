# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if id(headA) == id(headB):
            return headA
        tempA, tempB = headA, headB
        set_ = set()
        while tempA:
            set_.add(tempA)
            tempA = tempA.next
        while tempB:
            if tempB in set_:
                return tempB
            tempB = tempB.next
        return None