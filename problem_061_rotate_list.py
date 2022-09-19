from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or k == 0:
            return head

        current = head
        n = 1
        while current.next is not None:
            n += 1
            current = current.next

        k = k % n
        if n <= 1 or k == 0:
            return head
        last_node = current

        # now we have n - number of nodes
        current = head
        p = 1

        while p < n - k:
            current = current.next
            p += 1

        next_node = current.next
        current.next = None
        last_node.next = head
        return next_node


if __name__ == "__main__":
    input_lst = [1,2]
    k = 2
    head = ListNode(val=input_lst[0])
    current = head
    for val in input_lst[1:]:
        new_node = ListNode(val=val)
        current.next = new_node
        current = new_node

    s = Solution()
    ans = s.rotateRight(head, k)

    while ans is not None:
        print(ans.val, " ", end='')
        ans = ans.next
