import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, low, high):
            pivot_index = random.randint(low, high)   # pick random index
            nums[pivot_index], nums[high] = nums[high], nums[pivot_index]  # move pivot to end
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i + 1
        def quickSort(nums, low, high):
            if low < high:
                pivotIndex = partition(nums, low, high)
                quickSort(nums, low, pivotIndex - 1)
                quickSort(nums, pivotIndex + 1, high)
        quickSort(nums, 0, len(nums) - 1)
        return nums