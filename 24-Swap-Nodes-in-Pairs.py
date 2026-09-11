# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        def revTwo(prev): # [1, 2, 3, 4]
            curr = prev.next
            current_head = curr
            curr_tail = prev
            new_pair_head = None
            new_pair_tail = None
            if curr:
                new_pair_tail = curr.next
            if curr.next:
                new_pair_head = curr.next.next
            
            curr.next = prev

            prev.next = new_pair_head

            return current_head, curr_tail, new_pair_tail
        curr = head
        head = None

        while curr and curr.next:
            current_head, curr_tail, curr = revTwo(curr)
            if not head:
                head = current_head
        curr_tail.next = curr
        return head