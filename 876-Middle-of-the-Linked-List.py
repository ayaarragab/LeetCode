import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
            return head.next
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        if length % 2 == 0:
            length = length // 2
        else:
            length = math.ceil(length / 2)

        curr2 = head
        while curr2 and length > 0:
            curr2 = curr2.next
            length -= 1
        return curr2