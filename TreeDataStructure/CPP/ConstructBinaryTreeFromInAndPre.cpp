/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//to jest drzewo binarne, nie BST
//skrajny prawy element jest taki sam w obu, ale jak to wykorzystać?
//na nic dobrego nie wpadłem niestety
//na podstawie jenny lectures z yt, oraz komentarza użytkownika rashim-narayan-tiku 
//chciałem jeszcze zrobić po swojemu, by root był przekazywany jako parametr, ale nie dział
TreeNode * f( const vector<int> &A, map<int, int> &dict, int &Aidx, int INBegin, int INEnd ){
    if(INBegin > INEnd)return NULL;
    //tutaj kolejność bardzo istotna
    TreeNode *root = new TreeNode(A[Aidx]);
    Aidx +=1; //referencja!!
    if(INBegin==INEnd)return  root;
    
    
    root->left = f( A, dict, Aidx, INBegin, dict[root->val]-1); // lewa część indeksów
    root->right = f( A, dict, Aidx, dict[root->val]+1, INEnd );//prawa częśc indeksów
    
    return root;
}


//A to preorder, B to inorder
TreeNode* Solution::buildTree(vector<int> &A, vector<int> &B) {
    if(A.size()<1 || B.size() < 1)return NULL;
    map<int, int> dict; //klucz to wartość(w zadaniu jest, że unikalna), potem index
    int tempEnd = 0;
    for(int i=0; i<B.size(); i++){//słownik z indeksami z preorder, by nie szukać w pętli for indeksów
        dict[B[i]] = i;
    }
    int Aidx = 0;
    
    return f( A, dict, Aidx, 0, A.size()-1);
}