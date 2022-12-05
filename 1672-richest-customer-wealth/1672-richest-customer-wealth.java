class Solution {
    public int maximumWealth(int[][] accounts) {
        int sum, ans = Integer.MIN_VALUE;
        for (int i=0; i<accounts.length; i++){
            sum = 0;
            for (int j=0; j<accounts[i].length; j++){
                sum += accounts[i][j];
            }
            if (sum > ans){
                ans = sum;
            }
        }
        return ans;
    }
    
}