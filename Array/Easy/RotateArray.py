from typing import List

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        # reversing array
        self.rose(l, r, nums)

        l, r = 0, k - 1
        self.rose(l, r, nums)

        l, r = k, len(nums) - 1
        self.rose(l, r, nums)

    def rose(self, l, r, nums: List[int]):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

solution_instance = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

solution_instance.rotate(nums, k)
print(nums)

