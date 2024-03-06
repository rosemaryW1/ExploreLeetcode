from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l

# Creating an instance of the Solution class
solution_instance = Solution()

# Calling the removeDuplicates method on the instance
nums = [1,2,3,3,3,4,5,5,5]

result = solution_instance.removeDuplicates(nums)

print(nums[:result])