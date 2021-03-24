/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//początkowo chciałem BFS, ale pojawił się problem kiedy coś dopisywać do output, bo
//kolejka nie pozwalała na rozróżnienie, użyłem więc DFS root, right, left
/* dlatego najpierw obliczam wysokość drzewa, a potem skrajne elementy z prawej dopisuje
do output na odpowiednim indeksei(level) ale tylko jeśli element jest jest pusty
(oznaczone jako 0, choć powinienem użyć null), czyli skrajne lewe elementy są
sprawdzame na koncu

*/
void f(TreeNode *root, int level, vector<int>&output){
    
    if(root==NULL)return;
    // root, right, left
    if(output[level] ==0){
        output[level] = root->val;
    }
    
    if(root->right){
        f(root->right, level+1, output);
    }
    
    if(root->left)
        f(root->left, level+1, output);
    
}

int maxHeight(TreeNode *root){
    if(root==NULL)return 0;
    return 1 + max( maxHeight(root->left), maxHeight(root->right));
}

 
vector<int> Solution::solve(TreeNode* A) {
    
    TreeNode *root = A;
    int n = maxHeight(root);
    vector<int> output(n,0);
    
    queue<int> q;
    f(root, 0,  output);
    return output;
    
}
