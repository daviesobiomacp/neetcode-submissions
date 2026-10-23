class Solution:
    def isPalindrome(self, s: str) -> bool:
        #you want to use two pointers 
        #compare first and last then update first and last inward
        #use it till right before left is equal to right (while loop)
        #if l is not equal to r return false immediately
        #or return treu, (at the end)
        #remember to create the alphanumeric limit for comparison
        l,r = 0, len(s) -1 

        #iterate through using two pointers
        while l<r:
            #if l or r aren't alphanumeric
            while l<r and not self.alphaNumeric(s[l]):
                l += 1
            while r>l and not self.alphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        #final check for if everything works
        return True


    def alphaNumeric(self, c):
        return (ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9"))
        