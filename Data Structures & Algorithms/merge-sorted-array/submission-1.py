'''
1,1,3,6    2,5,7
       i       j
[1,1,2,3,5,6,7]
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #SOLUTION 1
        # mergedArr = []
        # i = 0
        # j = 0
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         mergedArr.append(nums1[i])
        #         i += 1
        #     else:
        #         mergedArr.append(nums2[j])
        #         j += 1
        # while i < m:
        #     mergedArr.append(nums1[i])
        #     i += 1
        # while j < n:
        #     mergedArr.append(nums2[j])
        #     j += 1
        # nums1[:] = mergedArr
        i = m - 1 #traverse from the back of nums1
        j = n - 1 #traverse from the back of nums2
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
       #fill nums1 with leftover nums2 elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

            
            

        