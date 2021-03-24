/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//wartosci w drzewie mogą być ujemne, dlatego nie ma warunku curSum > B
//mozna tez było zmniejszać B i porównywać z aktualnym rootem, do wyboru do koloru
void f(TreeNode *root, int curSum, int B, bool &output){
    if(root==NULL)return;
    if(root->left==NULL && root->right==NULL && curSum+root->val ==B){
        output=true;
        return;
    }
    
    f(root->left, curSum+root->val, B, output);
    f(root->right, curSum+root->val, B, output);

}
 
 
int Solution::hasPathSum(TreeNode* A, int B) {
    
    bool output = false;
    f(A, 0, B, output);
    return output;
}