from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or head is None:
            return head

        fake_head = ListNode(val=-1, next=head)
        prev, current = fake_head, head

        # go to left
        for pos in range(left-1):
            prev, current = current, current.next

        before_rev = prev
        prev = None

        # reverse
        for pos in range(right - left + 1):
            tmp = current.next
            current.next = prev
            prev, current = current, tmp

        before_rev.next.next = current
        before_rev.next = prev

        return fake_head.next


if __name__ == "__main__":
    input_lst = [3, 5]
    left, right = 1, 2

    head = ListNode(val=input_lst[0])
    current = head
    for val in input_lst[1:]:
        new_node = ListNode(val=val)
        current.next = new_node
        current = new_node

    s = Solution()
    ans = s.reverseBetween(head, left, right)

    while ans is not None:
        print(ans.val, " ", end='')
        ans = ans.next