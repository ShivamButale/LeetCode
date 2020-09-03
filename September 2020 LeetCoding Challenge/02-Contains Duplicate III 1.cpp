class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        vector<pair<int, int>> v1;
        int n = nums.size();
        for(int i=0;i<n;i++) {
            v1.push_back(make_pair(nums[i], i));
        }
        sort(v1.begin(), v1.end());
        for(int i=0;i<n-1;i++) {
            for(int j=i+1;j<n;j++) {
                if(v1[i].first+t < v1[j].first)
                    break;
                if(abs(v1[i].second - v1[j].second) <= k)
                    return true;
            }
        }
        return false;
    }
};
