from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """

          a.     b.     c
                 a      b     c.next
                              a     b.    c
                                    a.    b     c
        # 1 -->. 2 -->. 3 --> 4 --> 5


        # Remove this cyclic link
            --->
        # 1 <--  2 <--  3 <-- 4 <-- 5

        # 5 -->  4 --> 3 --> 2 --> 1
        """

        a = head
        b = head.next if head is not None else None
        c = head.next.next if b is not None else None

        if a is not None:
            a.next = None

        while b is not None:
            b.next = a

            a = b
            b = c
            c = c.next if c is not None else None

        return a
