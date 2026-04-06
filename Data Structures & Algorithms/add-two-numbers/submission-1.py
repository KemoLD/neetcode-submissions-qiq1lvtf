# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        head = dummy
        remainder = 0

        while l1 or l2 or remainder:

            if l1:
                remainder += l1.val
                l1 = l1.next

            if l2: 
                remainder += l2.val
                l2 = l2.next

            x = ListNode(remainder % 10)  # ones digit goes into node
            head.next = x
            head = head.next

            remainder = remainder // 10  # carry over


        return dummy.next