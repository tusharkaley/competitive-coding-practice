class Solution:
    def maxProfit(self, prices):
    	i = 0
    	j = 1
    	if len(prices)<=1:
    		return 0
    	max_profit = prices[j]-prices[i] if prices[i] < prices[j] else 0 

    	while j< len(prices):
    		if prices[j] <  prices[i]:
    			i = j
    			j = i+1
    		else:
    			max_profit = prices[j]-prices[i] if prices[j]-prices[i] > max_profit else max_profit
    			j=j+1
    	return max_profit





if __name__ == "__main__":
    s =  Solution()
    # ip = [7,1,5,3,6,4]
    # ip = [7,6,4,3,1]
    ip = [1,2]
    print(s.maxProfit(ip))