class Solution {
    public int findNumbers(int[] nums) {
        int cnt = 0;
        for (int i: nums){
           if (iseven(i)){
               cnt++;
           }
        }
        return cnt;
    }
    boolean iseven(int nums){
       int totalDigits = digitCount(nums);
        return totalDigits%2 == 0;
    }
    int digitCount(int nums){
        int cnt = 0;
        if (nums < 0){
            nums *= -1;
        }
        while(nums > 0){
            cnt++;
            nums /= 10;
        }
        return cnt;
    }
}