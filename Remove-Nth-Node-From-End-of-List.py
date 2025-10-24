# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if n == 1 and not head.next:
            return None

        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        turns = length - n + 1
        if n == length:
            new_head = head.next
            head.next = None
            return new_head
        i = 1
        current, prev = head, None
        while i < turns and current:
            prev = current
            current = current.next
            i += 1
        if prev and current:
            prev.next = current.next
            current.next = None
        return head