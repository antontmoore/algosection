from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        # 1. Find a middle point
        slow, fast = head, head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if prev_slow:
            prev_slow.next = None

        # 2. Reverse second part
        prev, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # 3. Merge two lists
        merged_head = ListNode()
        merged = merged_head
        first, second = head, prev
        while first or second:
            if first:
                merged.next = first
                first = first.next
                merged = merged.next
            if second:
                merged.next = second
                second = second.next
                merged = merged.next

        return merged_head.next


if __name__ == "__main__":
    input_lst = [1, 2, 3, 4]
    # input_lst = [1]

    head = ListNode(val=input_lst[0])
    current = head
    for val in input_lst[1:]:
        new_node = ListNode(val=val)
        current.next = new_node
        current = new_node

    s = Solution()
    ans = s.reorderList(head)

    while ans is not None:
        print(ans.val, " ", end='')
        ans = ans.next
