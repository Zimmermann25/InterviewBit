/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//to podejscie nie działa, nie ma mozliwości odróżnienia oziomów drzewa
/*void LRR(TreeNode * temp, vector<int> &LeftRootRight ){
    if(temp==NULL){
        LeftRootRight.push_back(INT_MIN);
        return;
    }
    LRR(temp->left, LeftRootRight);
    LeftRootRight.push_back(temp->val);
    LRR(temp->right, LeftRootRight);
}*/

/*void RRL(TreeNode * temp, vector<int> &RightRootLeft ){
    if(temp==NULL){
        RightRootLeft.push_back(INT_MIN);
        return;
    }
    
    RRL(temp->right, RightRootLeft);
    RightRootLeft.push_back(temp->val);
    RRL(temp->left, RightRootLeft);
}*/

/*Serio dosyć ciekawe zadanie, wydawałoby się, ze proste, ale jednak łatwe nie było

*/
bool f(TreeNode *temp1, TreeNode*temp2){
    if(temp1==NULL && temp2==NULL)return 1;
    else if(temp1==NULL)return 0;
    else if(temp2==NULL)return 0;
    else if(temp1->val != temp2->val)return 0;
    
    return f(temp1->left, temp2->right) && f(temp1->right, temp2->left);
    /*return int(root1.val == root2.val and helper(root1.left, root2.right) \
               and helper(root2.left, root1.right))*/
}

int Solution::isSymmetric(TreeNode* A) {
    
    /*vector<int> LeftRootRight;
    vector<int> RightRootLeft;
    LRR(A, LeftRootRight);*/
    //RRL(A, RightRootLeft);
    /*for(int i=0; i<RightRootLeft.size(); i++){
        if(RightRootLeft[i] != LeftRootRight[i])
            return 0;
    }*/
    
    /*for(int i=0; i<LeftRootRight.size(); i++){
        cout<<LeftRootRight[i]<<" ";
    }*/
    
    /*for(int i=0; i<LeftRootRight.size()/2; i++){
        if(LeftRootRight[i] != LeftRootRight[LeftRootRight.size() -1 - i]){
            return 0;
        }
    }*/
    if(A==NULL)return 1;
    return f(A->left, A->right);
}
