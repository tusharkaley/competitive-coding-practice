class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            # print(profit)
            if prices[i]> prices[j]:
                i= j
                j= i+1
            else:
                temp_p =prices[j]-prices[i]
                if temp_p > profit:
                    profit = temp_p
                j+=1
        return profit