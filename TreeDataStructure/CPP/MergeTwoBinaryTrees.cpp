/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
//po znalezieniu NULL jest problem, czy dodac z lewej, czy z prawej, nie sposób określić tego
//moze tak jak przy sprawdzaniu symetrii, wywyołać dla zewnętrznych i wewętrznych
//edit, symetria odpada, moze cos podobnego jak preorder(root, left, right)
//kierunek oznacza, czy dodać node po lewej, czy prawej (0-lewo, 1-prawo)
TreeNode * f(TreeNode* A, TreeNode* B){
    
    if(A==NULL)return B;
    if(B==NULL)return A;
    A->val += B->val; // nody sie pokrywają
    
    A->left = f(A->left, B->left);
    A->right = f(A->right, B->right);
    return A; // juz na koncu zwróć wskaźnik na root do odpowiedzi
}
 
//do drzewa A dodam drzewo B
TreeNode* Solution::solve(TreeNode* A, TreeNode* B) {
    
    
    return f(A,B);
}
