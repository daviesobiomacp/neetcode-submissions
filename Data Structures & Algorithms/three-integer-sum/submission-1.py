class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #return a list
        #sort the given list
        #use each number that is not repeating as the first
        #do two sum with the others
        #update the left or right pointer
        #return the list of lists

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            
            l,r = i+1, len(nums)-1

            while l<r:
                if a+ nums[l] + nums[r] > 0:
                    r-=1 
                elif a+ nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])           
                    r-=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1
        return res


        