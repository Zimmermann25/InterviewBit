/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
int f(TreeNode * temp){
    //musze znalezc leafNoed
    //dlatego są 4 warunki, 
    if (temp->left==NULL && temp->right==NULL){
        return 1;
    }
    else if(temp->left==NULL){
        //jakas duza liczba, zeby nie była brana do minimum
        return 1 + min( INT_MAX, f(temp->right) );
    }
    else if(temp->right==NULL){
        return 1 + min( f(temp->left), INT_MAX );
    }
    
    
    else{ // jak są 2 potomki
        return 1 + min( f(temp->left), f(temp->right) );
    }
    
}
 
int Solution::minDepth(TreeNode* A) {
    TreeNode* temp =A;
    if(temp==NULL)return 0;
    return f(temp);
}