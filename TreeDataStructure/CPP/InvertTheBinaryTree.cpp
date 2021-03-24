/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//tutaj zakładam, ze drzewo jest pełne, inaczej może być problem
//ja zrobiłem podejsciem BFS, ale podejscie DFS rzeczywiście tez będzie ok
// mozna to zrobic oczywiscie bez zewnętrznej funkcji, ale w tym kompilatorze czasami 
//cos działa, a czasami nie
void f(TreeNode* A){
    if (A==NULL)return;
    if(A->left && A->right){
        TreeNode* temp = A->left;
        A->left = A->right;
        A->right = temp;
    }
    
    if(A->left)
        f(A->left);
    if(A->right) // wcześniej nie było void, tylko TreeNode, wtedy tutaj musi byc return
       f(A->right); // tu musi byc return f(A->...), inaczej swiruje i nie działą
    
}
 
TreeNode* Solution::invertTree(TreeNode* A) {
    if(A==NULL)return NULL;
    f(A);
    return A;
}