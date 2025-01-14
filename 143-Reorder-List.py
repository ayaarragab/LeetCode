# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        \\\
        node = head
        if (not node.next) or (not node.next.next):
            return
        fast = node.next
        slow = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        ptr1 = None
        ptr2 = middle.next
        middle.next = None
        while ptr2:
            not_to_lose = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = not_to_lose
        ptr2 = ptr1
        ptr1 = node
        while ptr1 != ptr2:
            not_to_lose1 = None if not ptr1 else ptr1.next
            not_to_lose2 = None if not ptr2 else ptr2.next
            ptr1.next = ptr2
            if ptr1 and ptr1.next:
                ptr1.next.next = not_to_lose1
            ptr1 = not_to_lose1
            ptr2 = not_to_lose2
