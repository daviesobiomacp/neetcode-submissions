class Solution:
    def getSum(self, a: int, b: int) -> int:
        wrap = 0xFFFFFFFF
        max_Value = 0x7FFFFFFF
        while (b != 0):
            #temporarily store the carry fformula so you use original a to calculate with carries "&"
            temp = ((a & b) << 1) & wrap
            #calculate without carries "^"
            a = (a ^ b) & wrap
            #set b to be carries part
            b = temp & wrap
        #finally return a
        if a <= max_Value:
            return a
        
        else:
            return(~(a^wrap))
        