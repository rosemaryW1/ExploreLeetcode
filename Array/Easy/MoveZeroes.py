from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  you initialize the left pointer at index 0
        l = 0
        #  r will be a pointer through out the length of the array
        for r in range(len(nums)):
            # checking if the right pointer is a non zero element if it is you swap with the left
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                # Make sure to increament the left pointer
                l+=1
        return nums
solution_instance = Solution()

# Calling the removeDuplicates method on the instance
nums = [0,0,0,1,2,3]

result = solution_instance.moveZeroes(nums)

print(result)