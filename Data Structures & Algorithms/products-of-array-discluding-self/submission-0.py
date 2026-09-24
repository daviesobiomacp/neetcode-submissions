class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res





























        #create res array add prefic for each i then increase by multiple off next num,multiply each prefic by postfix then increase by multiple of next num
        