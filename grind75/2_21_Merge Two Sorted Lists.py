from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        list1:    1   ->   5   ->   7   ->   8   ->  9
        list2:    2   ->   4   ->   6

        """

        result = None
        result_head = None

        # what if one of the lists become empty
        # maintain the result head somehow

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                if result is None:
                    result = ListNode(list1.val)
                    result_head = result
                else:
                    result.next = ListNode(list1.val)
                    result = result.next
                list1 = list1.next
            else:
                if result is None:
                    result = ListNode(list2.val)
                    result_head = result
                else:
                    result.next = ListNode(list2.val)
                    result = result.next
                list2 = list2.next

        # either can be none

        while list1 is not None:
            if result is None:
                result = ListNode(list1.val)
                result_head = result
            else:
                result.next = ListNode(list1.val)
                result = result.next
            list1 = list1.next

        while list2 is not None:
            if result is None:
                result = ListNode(list2.val)
                result_head = result
            else:
                result.next = ListNode(list2.val)
                result = result.next
            list2 = list2.next

        return result_head
