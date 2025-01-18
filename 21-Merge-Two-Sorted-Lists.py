# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        node = None
        head = node
        while list1 and list2:
            if list1.val < list2.val:
                if not node:
                    node = list1
                    head = node
                else:
                    node.next = list1
                    node = node.next
                list1 = list1.next
            else:
                if not node:
                    node = list2
                    head = node
                else:
                    node.next = list2
                    node = node.next
                list2 = list2.next
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        return head