from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}
        for i, n in enumerate(nums):
            diff= target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

solution_instance = Solution()

nums = [2,7,11,15]
target = 9
result = solution_instance.twoSum(nums, target)
print(result)