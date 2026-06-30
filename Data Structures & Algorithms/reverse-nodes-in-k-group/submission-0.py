# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        # iterate until we have enough number of nodes
        # break when we have fewer nodes than k
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            # the start of the next group
            groupNxt = kth.next
            prev, curr = groupNxt, groupPrev.next
            # iterate until we get to the kth node or 
            # the node right after the kth node to avoid off by one error
            while curr != groupNxt:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            # update the new head to be the kth node
            groupPrev.next = kth
            # update groupPrev to be the node right before the start of the second group
            # which is the old start of the group
            groupPrev = tmp
        return dummy.next

    # get the end of the current group
    def getKth(self, curr, k):
        # checks if we have enough nodes to form a complete group
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

