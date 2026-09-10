# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Reverse each K consecutive nodes
        if not head or not head.next or k == 1:
            return head
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        num_of_turns = length // k
        def reverse_k_nodes(first, k):
            tail = first
            prev, curr = first, first.next
            while k > 1 and curr:
                save = curr.next
                curr.next = prev
                k -= 1
                prev, curr = curr, save

            return prev, tail, curr

        last_tail = None
        next_head = head
        head = None
        while num_of_turns != 0:
            curr_chain_head, curr_chain_tail, next_head = reverse_k_nodes(next_head, k)
            tail = curr_chain_tail

            if not head:
                head = curr_chain_head
            else:
                last_tail.next = curr_chain_head
            last_tail = curr_chain_tail
            num_of_turns -= 1

        if next_head:
            tail.next = next_head
            temp = next_head
        else:
            tail.next = None
        return head
