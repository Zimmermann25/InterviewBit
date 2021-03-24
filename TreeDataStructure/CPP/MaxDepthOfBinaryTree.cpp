/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
int f(TreeNode* A){
    
    if (!A)return 0; //base case

    return 1 + max(f(A->left), f(A->right));
}
 
 
int Solution::maxDepth(TreeNode* A) {
    if (A==NULL)return 0;

    return f(A);
}
