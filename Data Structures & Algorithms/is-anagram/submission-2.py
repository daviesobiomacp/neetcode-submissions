class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)

        listT.sort()
        listS.sort()

        return listS == listT
        