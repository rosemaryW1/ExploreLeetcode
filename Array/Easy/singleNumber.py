from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
solution_instance = Solution()

nums = [4,1,2,1,2]

res = solution_instance.singleNumber(nums)

print(res)
