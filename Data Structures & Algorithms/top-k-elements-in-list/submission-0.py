class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped = {}
        frequency = [[] for n in range(len(nums) + 1)]

        for n in nums:
            grouped[n] = 1 + grouped.get(n,0)
        for n, c in grouped.items():
            frequency[c].append(n)#elements with frequency of count
        res = []
        for i in range((len(frequency)-1),0,-1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                        return res
                        
                    
                    
































        #bucket sort problem
        #create the dictionary for the key value (numbers: frequency)
        #create array key value(frequency, numbers)
        #create final list and append final k elements
        