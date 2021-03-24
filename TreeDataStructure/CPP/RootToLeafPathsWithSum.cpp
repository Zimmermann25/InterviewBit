/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //pierwotny wynik z temp zamiast temp->left/right zwraca za dużo wartości
//preorder traversal powinienem użyć
//malutkie niedopełnienie było, które sprawiało, że miałem za duzo wyników
//choć były one poprawne i sumowały się do B
void f(TreeNode *root, int target, vector<int>temp, vector<vector<int>> &output){
    if(root == NULL ){
        return;
    }
    
    temp.push_back(root->val);
    
    if(root->left ==NULL && root->right==NULL && root->val==target){
        output.push_back(temp);
        return;
    }
    
    f(root->left, target - (root->val), temp, output);
    f(root->right, target - (root->val), temp, output);
    temp.pop_back(); // usuń aktualnie ostatnią dodaną wartość dziecka, które nie pasuje
    //po dojściu do liścia oczywiście
}
 
vector<vector<int> > Solution::pathSum(TreeNode* A, int B) {
    vector<vector<int>> output;
    vector<int> temp;
    f(A, B, temp, output);
    
    return output;
}