/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    int pathSum(TreeNode* root, int sum) {
        int ctr = 0;
        vector<int> v1;
        helper(root, sum, v1, ctr);
        return ctr;
    }
    
    void helper(TreeNode* root, int sum, vector<int> &v1, int &ctr) {
        if(!root)
            return;
        
        v1.push_back(root-> val);
        
        int curr_sum = 0;
        for(int i=v1.size()-1; i>=0; i--) {
            curr_sum += v1[i];
            if(curr_sum == sum) 
                ctr++;
        }
        
        helper(root->left, sum, v1, ctr);
        helper(root->right, sum, v1, ctr);
        
        v1.pop_back();
    }
    
};
