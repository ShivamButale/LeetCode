class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (root->val == key) {
            if (!root->left) {
                TreeNode* r = root->right;
                delete root;
                return r;
            }
            else {
                TreeNode* l = root->left;
                while (l->right)
                    l = l->right;
                swap(root->val, l->val);    
            }
        }
        root->left = deleteNode(root->left, key);
        root->right = deleteNode(root->right, key);
        return root;
    }
};
