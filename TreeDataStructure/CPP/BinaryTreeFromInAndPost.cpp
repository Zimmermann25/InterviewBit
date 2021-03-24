/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
//rozwiązanie praktycznie identyczne jak w preorder i inorder, tylko inna kolejność
//najpierw musze wypełniać prawe poddrzewa(bo root jest na końcu w postorder)
//postorder od ostatniego elementu sprawdzam
//z tego względu najpierw wywołuje root->right, a nie root->left
TreeNode * f(vector<int> &B, map<int, int> &dict, int &postID, int INBegin, int INEnd ){
    if(INBegin > INEnd)return NULL;
    TreeNode *root = new TreeNode(B[postID]);
    postID -=1;
    
    root->right = f(B, dict, postID, dict[root->val]+1, INEnd);
    
    if(INBegin == INEnd)return root;
    root->left = f(B, dict, postID, INBegin, dict[root->val]-1);
    
    
    return root;
}
 
//A to inorder, B to postorder, brak duplikatów
TreeNode* Solution::buildTree(vector<int> &A, vector<int> &B) {
    if(A.size() < 1 || B.size() < 1)return NULL;
    map<int, int> dict;
    for(int i=0; i<A.size(); i++){
        dict[A[i]] = i;
    }
    
    int postID = A.size()-1;
    return f(B, dict, postID, 0, A.size()-1);
}
