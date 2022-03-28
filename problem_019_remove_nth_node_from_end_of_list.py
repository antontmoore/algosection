from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        sz = 1
        cur_node = head
        while cur_node.next is not None:
            sz += 1
            cur_node = cur_node.next

        k = 0
        prev_node = None
        cur_node = head

        while k < sz - n:
            prev_node = cur_node
            cur_node = cur_node.next
            k += 1

        if k == 0:
            return head.next

        next_node = cur_node.next
        prev_node.next = next_node

        return head
