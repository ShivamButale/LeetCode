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
    vector<int> output;
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        helper(root1);
        helper(root2);
        sort(output.begin(), output.end());
        return output;
    }
    
    void helper(TreeNode* root) {
        if(root==NULL)
            return;
        output.push_back(root->val);
        helper(root->left);
        helper(root->right);
    }
};
