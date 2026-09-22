class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dictionary to store indices and values
        #check if the answer gotten fromn the subtrqacrtion between the target and a number  is already filled in the dictionsry
        #if it is, return (i,j)
        #else, return nothing because the question says the answer must be there
        twoSumHM = {}
        for i, j in enumerate(nums):
            difference = target - j
            if difference in twoSumHM:
                return [twoSumHM[difference],i]
            twoSumHM[j] = i
        return[]