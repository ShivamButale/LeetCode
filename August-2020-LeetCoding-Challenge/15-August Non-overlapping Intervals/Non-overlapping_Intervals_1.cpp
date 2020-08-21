bool comparator(vector<int> &a, vector<int> &b) {
    return a[1] < b[1];
}

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.size() == 0)
            return 0;
        int ctr = -1;
        sort(intervals.begin(), intervals.end(), comparator);
        vector<int> previous = intervals[0];
        
        for(auto i:intervals) {
            if(previous[1] > i[0]) {
                ctr+=1;
            }
            else  {
                previous = i;
            }
        }
        return ctr;
    }
};
