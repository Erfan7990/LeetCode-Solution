class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hst= new HashSet<Integer>();
        
        if(nums == null || nums.length == 0){
            return false;
        }
        for (int i: nums)
        {
            if(!hst.add(i)){
                return true;
            }
        }
        return false;
    }
}