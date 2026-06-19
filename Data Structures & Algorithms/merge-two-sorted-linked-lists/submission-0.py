# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2

        dummy = ListNode(0, None)
        curr = dummy # a moving pointer to build the new list

        while left and right:
            if left.val < right.val:
                curr.next = left
                curr = left
                left = left.next
            else:
                curr.next = right
                curr = right
                right = right.next
        while left:
            curr.next = left
            curr = left
            left = left.next
        while right:
            curr.next = right
            curr = right
            right = right.next
        return dummy.next
