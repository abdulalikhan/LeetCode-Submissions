class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pQueue(nums.begin(), nums.end());
        for (int i=0; i<k-1; ++i)
            pQueue.pop();
        return pQueue.top();
    }
};