from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        int1 = 0
        while l1 is not None:
            int1 += 10**i * l1.val
            l1 = l1.next
            i += 1

        i = 0
        int2 = 0
        while l2 is not None:
            int2 += l2.val * 10**i
            l2 = l2.next
            i += 1

        sum = int1 + int2
        reversed_sum = (str(sum))[::-1]

        head = ListNode(reversed_sum[0])
        curr = head

        for char in reversed_sum[1:]:
            new_node = ListNode(int(char))
            curr.next = new_node
            curr = new_node

        return head

    # based on https://leetcode.com solutions
    def addTwoNumbersBetter(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        curr = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0)

            if carry != 0:
                sum += 1
                carry = 0

            if sum >= 10:
                carry = 1
                sum = sum % 10

            new_node = ListNode(sum)
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next

class main:
    solution = Solution()

    num1_3 = ListNode(3)
    num1_2 = ListNode(4, num1_3)
    num1_1 = ListNode(2, num1_2)

    num2_3 = ListNode(4)
    num2_2 = ListNode(6, num2_3)
    num2_1 = ListNode(5, num2_2)

    num3_1 = solution.addTwoNumbersBetter(num1_1, num2_1)

    while num3_1 is not None:
        print(num3_1.val)
        num3_1 = num3_1.next
