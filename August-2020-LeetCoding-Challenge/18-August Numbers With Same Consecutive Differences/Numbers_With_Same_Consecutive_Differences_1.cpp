class Solution {
public:
    vector<int> numsSameConsecDiff(int N, int K) {
        vector<int>res; 
        if(N==1){
            for(int i=0;i<=9;i++){
                res.push_back(i) ;
            }
            return res;
        }
        
        
        
        
        int  ip = 0; 
        int len = 0 ; 
        solve(N,K,res,ip,len) ;
        return res;
    }
    
    void solve(const int &N,const int &K,vector<int>&res,int ip,int len){
        if(len>=N){
            res.push_back(ip);
            return ;
        }
        
        if(len==0){
            for(int i=1;i<=9;i++){
                ip= ip*10+ i;    
                solve(N,K,res,ip,len+1) ;
                ip=ip/10 ;
            }
        }else{
            int last = ip%10  ;
            int next = last+K ;
            int pre = last-K ;
            if(next<=9){
                ip = ip*10 +next ;
                solve(N,K,res,ip,len+1);
                ip=ip/10 ;
            }
            //next!=pre will fail at ===>N=2 and K=0 
            //O/P :[11,11,22,22,33,33,44,44,55,55,66,66,77,77,88,88,99,99]
            //Expected: [11,22,33,44,55,66,77,88,99]
            
            if(pre>=0 and next!=pre){ 
                ip = ip*10 +pre;
                solve(N,K,res,ip,len+1);
                ip=ip/10 ;
            }
            
            
             
        }
        
        
    }
};
