class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = 0
        profit = 0
        for i in range(len(prices)):
            if prices[lowest] > prices[i]:
                lowest = i
            if profit < prices[i] - prices[lowest]:
                profit = prices[i] - prices[lowest]
            
        return profit

#Time complexity: O(n) - n is the length of prices array
#Using a single simple loop we pass through each element exactly once.

#Space complexity: O(1) - we store a fixed number of variables
#We are only storing the lowest price encountered so far and the highest profit calculated.