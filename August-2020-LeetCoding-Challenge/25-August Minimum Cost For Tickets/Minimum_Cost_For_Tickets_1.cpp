class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int min_cost[366];
        min_cost[0]  = 0;
        unordered_map<int, bool> m1;
        for(auto day:days)
            m1[day] = true;
        for(int i=1;i<366;i++) {
            if(!m1[i])
                min_cost[i] = min_cost[i-1];
            else {
                int one = min_cost[i-1] + costs[0];
                int seven = min_cost[max(0, i-7)]+costs[1];
                int thirty = min_cost[max(0, i-30)] + costs[2];
                min_cost[i] = min(one, min(seven, thirty));
            }
        }
        return min_cost[365];
    }
};
