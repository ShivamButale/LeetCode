class Solution {
public:
    string getHint(string secret, string guess) {
        int A = 0, B = 0;
        unordered_map<char,int>mp;
        vector<int>include(guess.size(),false);
        
        for(int index = 0;index<secret.size();index++)
            if(secret[index]==guess[index])A++,include[index]=true;
            else mp[secret[index]]++;
        
       for(int index = 0;index<guess.size();index++)
           if(!include[index]&&mp[guess[index]]>0)B++,mp[guess[index]]--;
       
       return to_string(A)+'A'+to_string(B)+'B';
    }
};
