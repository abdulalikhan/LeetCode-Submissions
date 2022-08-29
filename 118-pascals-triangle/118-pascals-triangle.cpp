class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        int i, j;
        vector<vector<int>> pascalTriangle;
        for (i=0; i<numRows; ++i){
            vector<int> thisRow;
            for (j=0; j<i+1; ++j){
                if (j == 0 || j == i) 
                    thisRow.push_back(1);
                else if (i>0)
                    thisRow.push_back(pascalTriangle[i-1][j]+pascalTriangle[i-1][j-1]);
            }
            pascalTriangle.push_back(thisRow);
        }
        return pascalTriangle;
    }
};