class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    #create a master hashmap that has list default value
    #make count for each string 26 0 spaces
    #each string has its own count list as keys
    #add the strings of each similar count as values for keys

        anagrams = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char)-ord("a")] += 1
            anagrams[tuple(count)].append(string)
        return list(anagrams.values())

    
    