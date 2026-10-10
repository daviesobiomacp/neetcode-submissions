class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set your max profit to zero, sety your left and right pointers too
        #while l<r
        #check if it is profitable and if it is find max profit between the two
        #if not, make l to be the value of r now and update r
        #return max profit


        maxP = 0
        l,r = 0,1

        while l<r and r<len(prices):
            if prices[l]< prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1
        return maxP

        