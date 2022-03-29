from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        first_prev = None
        first = head
        second = head.next if head is not None else None

        while first is not None and second is not None:
            first.next = second.next
            second.next = first
            if first_prev is not None:
                first_prev.next = second
            else:
                head = second

            first_prev = first
            first = first.next if first.next is not None else None
            second = first.next if first is not None else None

        return head
