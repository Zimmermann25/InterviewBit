/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

void f(TreeNode*root, int curLevel, vector<int> &output){
    if(root==NULL)return;
    
    if(output.size() <= curLevel){//jak jeszcze nie ma tego indeksu to push_back
        output.push_back(root->val);
    }else{
        output[curLevel] += root->val;
    }
    
    f(root->left, curLevel+1, output);
    f(root->right, curLevel+1, output);
}
 
int Solution::solve(TreeNode* A) {
    vector<int>output;
    f(A, 0, output);
    int curMax = INT_MIN;
    for(int i=0; i<output.size(); i++){
        if(output[i] > curMax)curMax = output[i];
    }
    
    return curMax;
}
