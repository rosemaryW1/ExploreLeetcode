from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            if(i in nums2):
                output.append(i)
        return output

solution_instance = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

result = solution_instance.intersect(nums1, nums2)
print(result)