/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 

//inorder
/*bool traverse(TreeNode *first, TreeNode *second){
    if(first != NULL && second !=NULL)
        return (first->val==second->val && traverse(first->left, second->left ) && traverse(first->right, second->right));
    
    if(first==NULL && second==NULL)return 1; // liść
    
    return 0; // jak żaden z dwóch powyższych
}*/
 
bool traverse(TreeNode *first, TreeNode *second, bool &output){
    if(first != NULL && second !=NULL){
        if(first->val != second->val){
            output=0;
            return 0;
        }else{
            //tu był mój błąd, nie moge dać samego traverse(...), to nie void
            //musi być bool x1 = traverse(...)
            bool x1 = traverse(first->left, second->left, output );
            bool x2 = traverse(first->right, second->right, output );
            return (x1 && x2);
        }
        
    }
    //return (first->val==second->val && traverse(first->left, second->left ) && traverse(first->right, second->right));
    
    else if(first==NULL && second==NULL){
        //cout<<"elsif"<<endl;
        return 1; // liść
    }
    else{ // jeden jest NULL, ale drugi nie
       // cout<<"else";
        output = 0;
        return 0; // jak żaden z dwóch powyższych
    }
}
 
int Solution::isSameTree(TreeNode* A, TreeNode* B) {
    bool output = true;
    //return traverse(A, B, output);
    traverse(A, B, output);
    return output;
}
