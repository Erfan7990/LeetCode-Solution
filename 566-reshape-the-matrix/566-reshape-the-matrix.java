class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int row = mat.length;
        int col = mat[0].length;
        int[][] arr = new int[r][c];
        int newCol=0, newRow=0;
            
        if (row*col != r*c)
        {
            return mat;
        }
        
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                arr[newRow][newCol] = mat[i][j];
                newCol++;
                
                if (newCol == c){
                    newCol=0;
                    newRow++;
                }
            }
        }
        return arr;
    }
}