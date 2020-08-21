#include <vector>
class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> v1(num_people);
        int curr=1;
        int i=0;
        while(candies) {
            if(candies < curr) {
                curr = candies;
            }
            v1[i%num_people] += curr;
            candies=candies-curr;
            i++;
            curr++;
        }
        return v1;
    }
};
