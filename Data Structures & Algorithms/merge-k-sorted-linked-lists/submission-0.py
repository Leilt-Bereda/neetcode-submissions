# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = [] # save the merged lists for the next itreration
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # handle the edge case where i goes out of bounds
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                mergedLists.append(self.merge(l1,l2))
            # update lists to be mergedLists 
            # so the next round of the while loop uses the new smaller list
            lists = mergedLists
        return lists[0]
    def merge(self, l1, l2):
        dummy = ListNode(0, None)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

