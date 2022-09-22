from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None: return head

        prev, current = None, head

        while current is not None and current.next is not None:
            if current.next.val != current.val:
                prev = current
                current = current.next
                continue

            while current.next is not None and current.next.val == current.val:
                current = current.next

            next_node = current.next if current.next else None
            if prev:
                prev.next = next_node
            else:
                head = next_node
            current = next_node

        return head
