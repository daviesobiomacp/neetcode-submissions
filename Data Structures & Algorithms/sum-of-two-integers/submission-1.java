class Solution {
    public int getSum(int a, int b) {
        //create a limit
         while (b != 0){
            //temporarily store the carry fformula so you use original a to calculate with carries "&"
            int temp = (a & b) << 1;
            //calculate without carries "^"
            a = (a ^ b);
            //set b to be carries part
            b = temp;
         }
        //finally return a
        return a;
    }
}
