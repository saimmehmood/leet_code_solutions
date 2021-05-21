class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        profit = 0 
        
        for i in range(len(prices) - 1):
            
            # checking if the price on previous day is less
            if prices[left] <= prices[right]:
                # keeping the maximum profit
                profit = max(profit, prices[right] - prices[left])
                right += 1
                
            else:
                # move both left and right pointer forward
                left = right
                right += 1
        
        return profit
