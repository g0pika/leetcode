class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mn = 10000
        mx = 0
        for i in prices:
            if i < mn:
                mn = i
            else:
                diff = i - mn
                if profit < diff:
                    profit = diff
                    
        return profit
                    
