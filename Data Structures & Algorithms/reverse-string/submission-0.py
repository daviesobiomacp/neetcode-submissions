class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        #you want to use two pointers
        #from beginning of string and swap with end 
        #when l is finally equal to r you stop
        #don't return just sway values

        l, r = 0, len(s)-1
        while (l<r):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l+=1
            r-=1
        

        