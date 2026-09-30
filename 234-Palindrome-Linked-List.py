class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
    
        def reverse(curr):
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        other_half_head = reverse(slow)

        c1, c2 = head, other_half_head

        while c1 and c2:
            if c1.val != c2.val:
                return False
            c1 = c1.next
            c2 = c2.next
        return True