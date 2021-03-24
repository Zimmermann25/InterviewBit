/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//to co chce napisac z wykorzystaniem kolejki nie zadziała, problemem są poddrzewa lewych dzieci
//root, right, left

//zwrociło błędnie 29 15 4 29 29 10 28 28 4 
//Edit, teraz jest już poprawnie, sprawdzenie w komentarzach, czy była możliwość 
//zobienia używając kolejki: tak była, w dodatku bez rekurencji, czym zacząłem się kierować
//choć ktoś również użył kolejki i rekurencji
void f(TreeNode* root, queue<TreeNode* > &q, vector<int> &output){
    if(root==NULL)return;
    
    //idz mozliwie w prawo, prawe elementy do output, lewe do kolejki
    q.push(root);
    while(q.size() > 0){
         TreeNode * temp = q.front();
         q.pop();
        
        //idz w prawo
        while(temp !=NULL){
            output.push_back(temp->val);
            if(temp->left !=NULL)q.push(temp->left);
            temp = temp->right;
        }
    }
}

vector<int> Solution::solve(TreeNode* A) {
    
    vector<int> output;
    queue<TreeNode* > q;
    f(A, q, output);
    return output;
}


//ten kod z komentarza już cięższy jest, można go zrozumieć, ale ciężej samemu wpaść
/*queue<TreeNode* > s;

void helper(vector &ans , TreeNode *a){
    if(a==NULL)
        return;
    if(a->left){
        s.push(a->left);
    }
    ans.push_back(a->val);
    if(a->right!=NULL)
        helper(ans,a->right);
    else{
        while(!s.empty()){
            TreeNode *temp = s.front();
            ans.push_back(temp->val);
            s.pop();
            
            if(temp->left)
                s.push(temp->left);
            if(temp->right)
                helper(ans,temp->right);
        }
    }
}*/