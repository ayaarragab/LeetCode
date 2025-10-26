# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if head and not head.next:
            return head
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head
        turns = k % length
        steps_to_new_tail = length - turns - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        head = new_tail.next
        new_tail.next = None
        return head