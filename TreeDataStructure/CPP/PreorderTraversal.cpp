/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<int> Solution::preorderTraversal(TreeNode* A) {
    
    vector<TreeNode* > s;
    s.push_back(A);
    vector<int> output;
    //niesamodzielne, tutaj nie mozna było mysleć schematem root, left, right
    //na stos wchodzą najpierw wartości po prawej, potem te po lewej
    //po zdjęciu te prawe są obslugiwane już w poprawnej kolejności
    
     while(!s.empty()){
        TreeNode* temp = s[s.size()-1];
        s.pop_back();
        output.push_back(temp->val);
        if(temp->right!=NULL){
            s.push_back(temp->right);
        }
        if(temp->left!=NULL){
            s.push_back(temp->left);
        }
    }

    
    /*while (!s.empty() or temp!=NULL){
        if(temp){
            output.push_back(temp->val);
            s.push_back(temp);
            temp = temp->left;
        }
        else{
            if(!s.empty()){
                temp = s[s.size()-1];
                s.pop_back();
            }
            
            temp = temp->right;
            int curVal = temp->val;
            output.push_back(curVal);
            
            s.push_back(temp);
        }
    }*/
    
    return output;
}