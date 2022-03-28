from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        cur_node = head
        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                cur_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur_node.next = ListNode(list2.val)
                list2 = list2.next

            cur_node = cur_node.next

        if list1:
            cur_node.next = list1

        if list2:
            cur_node.next = list2

        return head.next
