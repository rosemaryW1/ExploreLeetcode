from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

solution_instance = Solution()

nums = [1,2,3,4,2,1]

result = solution_instance.containsDuplicate(nums)

print(result)