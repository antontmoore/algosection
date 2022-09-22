from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None: return head

        current_node = head

        while current_node.next is not None:
            next_node = current_node.next
            if current_node.val == next_node.val:
                current_node.next = next_node.next
            else:
                current_node = next_node

        return head