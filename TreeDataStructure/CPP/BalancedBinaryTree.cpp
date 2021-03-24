/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 /*swietne rozwiązanie z komentarza
 int res = 1;
int F(TreeNode *A)
{
    if(A == NULL) return 0;
    
    int lh = F(A->left);
    int rh = F(A->right);
    
    if(abs(lh - rh) > 1) res = 0; 
    return max(lh, rh) + 1;
}
int Solution::isBalanced(TreeNode* A) 
{
    res = 1;
    F(A);
    
    return res;
}*/
 
//moj pomysł, niestety coś nie działa :(
/*void f(TreeNode *temp, int leftHeight, int rightHeight, bool &output){
    if(abs(leftHeight - rightHeight) > 1)output=false;
    
    if(temp->left && temp->right){
        f(temp->left, leftHeight+1, rightHeight+1, output);
        f(temp->right, leftHeight+1, rightHeight+1, output);
    }
    else if(temp->left){
        f(temp->left, leftHeight+1, rightHeight, output);
    }
    else if(temp->right){
        f(temp->right, leftHeight, rightHeight+1, output);
    }
    else return; // brak dzieci
 }*/
 
int height(TreeNode *temp){
    if (temp==NULL)return 0;
    return 1 + max( height(temp->left), height(temp->right) );
}
//zlozonosc N^2, dla kazdego node licz wysokości i porównuj
//niezbyt efektywne, bo wiele obliczen się powtarza
void f(TreeNode *temp, bool &output){
    if(temp==NULL)return;
    int leftHeight = height(temp->left);
    int rightHeight = height(temp->right);
    
    //cout<<"left: "<<leftHeight<<" right: "<<rightHeight<<endl;
    if(abs(leftHeight - rightHeight) >1){
        output = false;
        return;
    }
    
    f(temp->left, output);//wywołaj liczenie wysokości dla dzieci jako root
    f(temp->right, output);
    
}
 
int Solution::isBalanced(TreeNode* A) {
    //potrzebuje różnicy w wysokościach
    TreeNode* temp = A;
    bool output = true;
    f(temp, output);
    return output;
    
}