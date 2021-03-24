/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//tutaj może być DFS, albo BFS, dfs z dowolną kolejnością, ja użyłem preorder 
//zapis z dodatkowym wektorem output wygląda brzydko, ale działa
void f(TreeNode *root,int B, vector<int> tempArr, vector<int> &output){
    
    if(root==NULL)return;
    if(root->val == B){
        output = tempArr;
        output.push_back(B); //z docelowym elementem włącznie
        //cout<<"found"<<endl;
        return;
    }
    
    tempArr.push_back(root->val);
    f(root->left, B, tempArr, output);
    f(root->right, B, tempArr, output);
}
 
vector<int> Solution::solve(TreeNode* A, int B) {
    
    
    vector<int> output;
    TreeNode *root = A;
    vector<int> tempArr;
    f(root,B, tempArr, output);
    return output;
}