public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) 
        {
            // Extract the least significant bit
            int bit = n & 1;   

            // Append the bit to the result      
            result = (result << 1) | bit; 
            
            // Unsigned right-shift
            n = n >>> 1;             
        }
        return result;
    }
}
