class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def get_length(head):
            curr = head
            l = 0
            while curr:
                curr = curr.next
                l += 1
            return l
        
        def is_same_element(k, length):
            return k == (length - k + 1)
        
        def get_prev_nth(head, n):
            if not n:
                return None
            curr = head
            cnt = 1
            while curr:
                if cnt == n - 1:
                    return curr
                curr = curr.next
                cnt += 1
            return curr
    
        def insert_front(head):
            old_head = head
            new_head = ListNode(0)
            new_head.next = head
            head = new_head
            return old_head, new_head
        
        def delete_front(head):
            save = head.next
            head.next = None
            head = save
            return head
    
        def swap(prev_one, prev_two, head):
            if prev_one:
                one = prev_one.next
            else:
                one = head
            if prev_two:
                two = prev_two.next
            else:
                two = head

            save1 = one.next
            save2 = two.next

            if one.next == two:
                one.next = save2
                two.next = one
                if prev_one:
                    prev_one.next = two
                return
            if two.next == one:
                two.next = save1
                one.next = two
                if prev_two:
                    prev_two.next = one
                return
            one.next = save2
            two.next = save1
            prev_one.next = two
            prev_two.next = one

        length = get_length(head)
        if length < 2 or is_same_element(k, length):
            return head
        length += 1
        old_head, new_head = insert_front(head)

        one_prev = get_prev_nth(old_head, k)
        two_prev = get_prev_nth(old_head, length - k)

  
        if k <= (length - 1) // 2:
            swap(one_prev, two_prev, old_head)
        else:
            swap(two_prev, one_prev, old_head)
        
        head = delete_front(new_head)
        return head

