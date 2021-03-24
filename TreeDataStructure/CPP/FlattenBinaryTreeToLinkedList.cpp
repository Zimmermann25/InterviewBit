/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//root, left, right
//pomysł polaga na tym, że przepinam lewe poddrzewo, potem na jego prawym końcu dopinam
//prawe poddrzewo, którego miejsce zostało zajęte 
void f(TreeNode *temp){
    if(temp==NULL)return;
    TreeNode *curRight = temp->right;//zapamietaj prawe poddrzewo
    TreeNode *curLeft = temp->left;//zapamietaj lewe poddrzewo
    //jak jest lewe podrzewo, to je przepnij i na jego koncu po prawej dołącz prawe poddrzewo
    
    if(temp->left !=NULL){
        temp->right = temp->left;//przepnij lewe poddrzewo jako prawe
        
        //traverse przepiętego lewego do konca, by dopiąć na prawym liściu zapamiętane prawe
        while(curLeft->right !=NULL){
            curLeft = curLeft->right;
        }
        
        //dopnij zapamiętane prawe poddrzewo do wstawionego lewego
        curLeft->right = curRight;
        
        temp->left = NULL;//wyzeruj lewe poddrzewo aktualnego node
        
    }
    
    
    f(temp->right);
}
 
TreeNode* Solution::flatten(TreeNode* A) {
    
    TreeNode *root = A;
    f(root);
    
    return root;
}