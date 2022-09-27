from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        current, prev = head, ListNode(val=0, next=head)
        before_head = prev
        new_list = ListNode()
        new_list_before_head = new_list

        while current is not None:
            if current.val < x:
                prev.next = current
                prev = current
            else:
                # put it to new list
                new_list.next = current
                new_list = new_list.next

            current = current.next

        new_list.next = None

        prev.next = new_list_before_head.next
        return before_head.next


if __name__ == "__main__":
    input_lst = [1, 4, 3, 2, 5, 2]
    x = 3
    head = ListNode(val=input_lst[0])
    current = head
    for val in input_lst[1:]:
        new_node = ListNode(val=val)
        current.next = new_node
        current = new_node

    s = Solution()
    ans = s.partition(head, x)

    while ans is not None:
        print(ans.val, " ", end='')
        ans = ans.next
