# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        new = ListNode(0, head)
        first = new
        second = new

        while second and second.next:
            first = first.next
            second = second.next.next

        prev = None
        curr = first.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first.next = None
        one = head
        two = prev

        while two:
            tmp1 = one.next
            tmp2 = two.next
            one.next = two
            two.next = tmp1
            one = tmp1
            two = tmp2

    #return new.next


        