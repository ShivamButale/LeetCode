class Solution {
public:
    vector<int> partitionLabels(string S) {
        int n = S.size();
        vector<int> partitions;
        
        if(n==0)
            return partitions;
        
        vector<int> last_occ(26, -1);
        for(int i=n-1;i>=0;i--) {
            if(last_occ[S[i] - 'a'] == -1) 
                last_occ[S[i]-'a'] = i;
        } 
        
        int min_pos = -1, part_len=0;
        for(int i=0;i<n;i++) {
            int curr = last_occ[S[i]-'a'];
            min_pos = max(curr, min_pos);
            part_len++;
            
            if(i==min_pos) {
                partitions.push_back(part_len);
                min_pos = -1;
                part_len = 0;
            }
        }
        
        return partitions;
    }
};
