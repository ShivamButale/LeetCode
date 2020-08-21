class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n = nums.size();
        vector<int> v1;
        for(int i=0;i<n;i++) {
            if(nums[abs(nums[i])-1] < 0)
                v1.push_back(abs(nums[i]));
            nums[abs(nums[i])-1] =- nums[abs(nums[i])-1];
        }
        return v1;
    }
};
