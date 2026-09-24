class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length 

        return res
            















        #encode: you want your output to be a string. for each value in the string, write the lenghth before it, and hash after the length. make sure you use the string function on the integer


#decode you want your output to be a list so use the integer at the front(make sure to convert from integer to string) then find lengtjh and use from i which is j and as long as j is not equal to the hash, you keep increasing by 1. then for the length of each list you do starting point(j+1) to j + 1 + integer