# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        \\\
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        if not list1:
            return list2
        if not list2:
            return list1
        head = list1
        last_in_list1 = head
        while last_in_list1.next:
            last_in_list1 = last_in_list1.next
        last_in_list1.next = list2
        if not head.next.next:
            if head.val > head.next.val:
                temp = head
                head = head.next
                head.next = temp
                temp.next = None
                return head
            elif head.val <= head.next.val:
                return head
        back = None
        swap = True
        fixed = head
        prev = fixed
        _next = prev.next
        while fixed and swap:
            swap = False
            back = None
            fixed = head
            prev = fixed
            _next = prev.next
            swaps = []
            while _next:
                if prev.val > _next.val:
                    save = _next.next
                    if not back:
                        first_node = True
                        prev.next = save
                        _next.next = prev
                        back = _next
                        head = back
                        if prev == fixed:
                            fixed = _next
                    else:
                        first_node = False
                        back.next = _next
                        _next.next = prev
                        prev.next = save
                    swaps.append(True)
                    temp = _next
                    _next = prev
                    prev = temp
                else:
                    if not back:
                        back = head
                        first_node = True
                    else:
                        first_node = False
                    swaps.append(False)
                if not _next.next:
                    if any(swaps):
                        swap = True
                    else:
                        swap = False
                back = back.next if not first_node else back
                prev = prev.next
                _next = _next.next if _next else None
        return head