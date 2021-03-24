/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<int> Solution::inorderTraversal(TreeNode* A) {
    //rekurencja przypomina stos
    //musiałbym niszczyc drzewo tę metodą, którą chce uzyc, co jest bez sensu 
    vector<TreeNode*> s;
    vector<int>output;
    TreeNode* temp = A;
    
    //te dwa warunki są wymagane, bo temp prędzej czy pozniej będzie NULL,
    //ale jesli coś jest na stosie, to trzeba kontynuować
    while ( !s.empty() || temp!=NULL ){

        if (temp){
            s.push_back(temp);
            temp = temp->left;
        }
        else{
            if( !s.empty()){
                int curVal = s[s.size() -1]->val;
                output.push_back(curVal);
            }
            
            temp = s[s.size()-1]->right;//kolejnosc wazna tutaj
            s.pop_back();
            
        }
        
        
        
    }
    
    /*while(stack !=[] or t!=None):
        if(t!=None):
            stack.append(t)
            t=t.left
        else:
            t=stack.pop()
            inorder.append(t.val)
            t=t.right
    return inorder*/
        
    
    
    return output;
}