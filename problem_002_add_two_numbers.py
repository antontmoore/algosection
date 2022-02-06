# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        empty_head = ListNode(0)
        sum_list = empty_head

        carry = 0
        while l1 is not None or l2 is not None:
            l1value = l1.val if l1 is not None else 0
            l2value = l2.val if l2 is not None else 0
            sum_value = l1value + l2value + carry

            carry = sum_value // 10
            sum_value = sum_value % 10

            sum_list.next = ListNode(sum_value)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            sum_list = sum_list.next

        if carry:
            sum_list.next = ListNode(1)

        return empty_head.next
