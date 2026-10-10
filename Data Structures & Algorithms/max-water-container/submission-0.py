class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #store your res as 0
        #setup you left and right pointers
        #set area to be higher using max between res and area
        #while l< r use left and right pointers and if area is less update based on which is bigger between l and r
        #return area at the end

        res = 0 
        l, r = 0, len(heights) - 1

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l]< heights[r]:
                l += 1
            else:
                r-=1
        return res

        