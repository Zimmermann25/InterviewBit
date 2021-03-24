/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //czy to jest taka jakby funkcja insert, podone do avl, ale łatwiejsze, bo sorted arr
 //edit, jednak można łatwiej
/*void f(TreeNode *temp, int curVal ){
    
    //najpierw wstawienie
    while(temp !=NULL){
        if(temp->left==NULL, temp->right==NULL){ // leaf node
            if(curVal > temp->val){
                
            }
        }
        if(curVal > temp->val)
            temp = temp->right;
        else
            temp = temp->left;
    }
    //potem wyrównanie balansu
}*/


//ta funkcja to coś w stylu merge sort, element środkowy to będzie root i potem podtablice
//tutaj największy problem miałem z kodowaniem i faktem co zrobić z rootem
//bo w tym edytorze to jest dramat
//troche dziwny i mało intuicyjny ten kod mementami się wydaje, ale działa
TreeNode *f(const vector<int> &A, int start, int stop){
    
    int mid = (start + stop)/2;
    if ( start>stop || mid < 0 || mid >= A.size())return NULL;
    TreeNode * curRoot = new TreeNode(A[mid]);
    
    curRoot->left = f( A, start, mid-1);
    curRoot->right = f( A, mid+1, stop);
    return curRoot; // wartosc mid oryginalna będzie zwrócona na koncu, ze wzgledu na 
    //wyglad drzewa wywołań
}
 
TreeNode* Solution::sortedArrayToBST(const vector<int> &A) {
    if(A.size() == 0)
        return NULL;
    if(A.size() == 1)
    {
        TreeNode *root = new TreeNode(A[0]);
        return root;
    }

    return f(A, 0, A.size()-1); // ten -1 ważny, bo działam na indeksach
}