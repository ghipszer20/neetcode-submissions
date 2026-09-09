class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = len(prices) - 1
        j = i - 1

        while j >= 0:
            if prices[j] > prices[i]:
                i = j
                j -= 1
            else:
                max_profit = max(max_profit, prices[i] - prices[j])
                j -= 1

        return max_profit
        