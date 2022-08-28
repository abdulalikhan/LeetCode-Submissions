class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> numMap;
        int n = nums.size();
        for (int i=0; i<n; ++i){
            if (++numMap[nums[i]] > n/2)
                return nums[i];
        }
        return -1;
    }
};