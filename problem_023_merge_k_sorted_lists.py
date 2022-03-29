from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        cur_node = head
        while any(lists):
            min_val = min([x.val if x is not None else 1e4 for x in lists])
            min_ind = 0
            for ind, l in enumerate(lists):
                if l is not None and l.val == min_val:
                    min_ind = ind
                    break

            cur_node.next = ListNode(val=lists[min_ind].val)
            cur_node = cur_node.next
            lists[min_ind] = lists[min_ind].next
            if lists[min_ind] is None:
                lists.pop(min_ind)

        return head.next
