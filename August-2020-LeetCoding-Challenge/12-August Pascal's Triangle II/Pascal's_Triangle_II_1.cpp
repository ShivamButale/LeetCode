#include <vector>
#include <bits/stdc++.h>
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> result(rowIndex+1);

        for(int i=0;i<=rowIndex;i++) {
            result[i].resize(i+1);
            result[i][0] = result[i][i] = 1;
            for(int k=1;k<i;k++) {
                result[i][k] = result[i-1][k-1] + result[i-1][k];
            }
        }
        return result[rowIndex];
    }
};
