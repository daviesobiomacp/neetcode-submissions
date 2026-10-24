class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #you want to have two pointers, one for each word
        #while length of the words are equal, you want to append normally
        #you want to use an array since strings are immutable
        ##you want to append the letters each to the list you made with ""join
        #when they are not, you want to try add letters from both in case
        #finally, you want to return the list


        l, r = 0, 0
        res = []

        while (l < len(word1) and r < len(word2)):
            res.append(word1[l])
            res.append(word2[r])

            l+=1
            r+=1
        res.append(word1[l:])
        res.append(word2[r:])
        
        return "".join(res)

        