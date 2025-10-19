# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        set_ = set()
        
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val == head.next.val:
                head.next = None
            return head
        prev, current = None, head
        while current:
            if current.val not in set_:
                set_.add(current.val)
                prev = current
                current = current.next
            else:
                save = current.next
                prev.next = save
                current.next = None
                current = save
        return head