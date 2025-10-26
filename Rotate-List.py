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
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        turns = k % length
        current = head
        for _ in range(turns):
            while current.next.next:
                current = current.next
            new_head = current.next
            current.next.next = head
            current.next = None
            head = new_head
            current = new_head
        return head