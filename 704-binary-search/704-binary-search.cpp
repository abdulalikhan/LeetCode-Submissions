class Solution {
public:
    int binarySearch(vector<int>& nums, int target, int lowerBound, int upperBound){
        if (lowerBound > upperBound)
            return -1;
        int mid = (lowerBound+upperBound)/2;
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] > target)
            return binarySearch(nums, target, lowerBound, mid-1);
        else
            return binarySearch(nums, target, mid+1, upperBound);
    }
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, target, 0, nums.size()-1);
    }
};