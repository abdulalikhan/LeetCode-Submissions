class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int total = nums.size()*(nums.size()+1)/2, c=0;
        for (int i=0; i<nums.size(); ++i)
            c += nums[i];
        return total-c;
    }
};