from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit

solution_instance = Solution()
prices = [1, 7, 3, 5, 1, 4]

result = solution_instance.maxProfit(prices)

print(result)