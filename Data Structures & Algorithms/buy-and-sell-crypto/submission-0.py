class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        leftpointer=0
        rightpointer=1

        currentmaxprofit=0

        while rightpointer<len(prices):

                if prices[rightpointer]>prices[leftpointer]:
                    profit=prices[rightpointer]-prices[leftpointer]
                    currentmaxprofit=max(profit,currentmaxprofit)

                else:
                    leftpointer=rightpointer

                rightpointer+=1    

        return currentmaxprofit

        