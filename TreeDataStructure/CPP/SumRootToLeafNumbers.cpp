/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 //błędne rozwiązanie po złej interpretacji zadania
 /*void f(TreeNode*temp, int curVal, int &output){
    //cout<<"curVal: "<<curVal<<" output: "<<output<<endl;
    //if(temp==NULL)return;//by nie sprawdzac dalej tej gałęzi
    
    //MUSZE znalezc liścia i dopiero wtedy dodać
    if(temp->left==NULL && temp->right==NULL){
        //XDD, wyrażenie curVal*10 + temp-> val było i kompilator nie zwrócił błędu xdddd
        //po dopisaniucurVal = ... działa
        curVal = (curVal*10 + temp->val + 1003) % 1003;
        output += curVal;
        output = (output + 1003) % 1003; // dla bezpieczenstwa
        return;
    }
    if(temp->left !=NULL)
        f(temp->left, curVal*10 + temp->val, output);
    if(temp->right !=NULL)
        f(temp->right, curVal*10 + temp->val, output);
}*/
 /*763 3 7 9 9 0 -1 -1 2 1 4 3 2 5 2 2 4 8 1 1 4 9 0 -1 8 3 5 2 5 -1 1 6 2 8 1 0 7 3 -1 7 -1 6 6 1 7 1 5 9 4 7 -1 7 -1 -1 -1 6 2 8 7 8 1 5 9 0 4 6 -1 -1 5 6 -1 2 1 8 2 5 5 -1 4 -1 1 9 1 4 3 5 7 4 -1 -1 0 6 7 5 -1 2 1 7 1 9 0 2 5 4 -1 -1 -1 -1 -1 8 2 2 -1 -1 -1 -1 -1 2 -1 3 9 4 8 8 6 4 7 2 5 7 1 -1 9 5 3 8 0 4 -1 -1 5 5 7 2 -1 -1 -1 8 0 4 4 5 5 7 -1 -1 5 6 3 -1 9 1 9 -1 8 -1 -1 9 -1 -1 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 6 7 3 -1 1 8 -1 -1 1 8 -1 -1 -1 8 0 0 5 6 -1 -1 0 -1 9 -1 5 -1 6 6 -1 6 2 6 5 -1 -1 7 3 1 6 -1 7 6 -1 -1 6 -1 3 9 -1 -1 -1 0 -1 2 -1 0 -1 7 3 5 -1 8 2 0 6 8 7 3 9 0 1 0 -1 -1 -1 0 8 7 2 9 -1 6 6 6 -1 2 3 2 -1 -1 1 1 4 8 -1 2 0 -1 -1 -1 -1 -1 -1 1 3 6 -1 -1 -1 -1 5 4 1 7 7 -1 -1 -1 -1 -1 -1 0 8 0 -1 5 5 -1 7 3 -1 -1 1 -1 -1 -1 7 9 4 -1 4 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 0 5 5 -1 -1 -1 2 6 8 1 -1 0 -1 6 -1 0 -1 -1 -1 -1 -1 -1 6 8 2 -1 4 2 -1 1 -1 -1 -1 2 1 0 2 7 8 -1 1 -1 -1 3 4 -1 -1 -1 -1 -1 5 -1 -1 8 2 -1 -1 -1 -1 2 8 -1 3 -1 8 6 3 -1 -1 -1 8 6 4 -1 -1 -1 -1 5 -1 -1 -1 -1 -1 -1 9 4 -1 -1 -1 -1 -1 -1 -1 2 2 7 3 9 -1 -1 9 -1 -1 -1 -1 6 -1 3 8 -1 -1 -1 -1 -1 -1 -1 3 -1 -1 -1 -1 -1 -1 -1 -1 4 -1 2 -1 -1 -1 -1 2 -1 -1 1 9 1 -1 -1 2 5 1 -1 -1 4 2 -1 -1 -1 7 6 3 8 2 8 -1 -1 0 -1 -1 3 1 -1 -1 5 -1 -1 9 -1 2 -1 0 -1 -1 -1 8 -1 -1 8 -1 -1 0 -1 0 -1 7 -1 -1 1 4 -1 9 5 3 -1 -1 -1 2 3 -1 -1 -1 6 7 -1 0 6 -1 -1 -1 -1 -1 5 -1 -1 -1 5 -1 -1 -1 -1 -1 4 8 3 -1 -1 9 5 -1 -1 -1 9 0 -1 -1 -1 -1 -1 -1 -1 -1 4 -1 7 -1 -1 -1 -1 -1 -1 -1 4 0 -1 8 1 -1 5 -1 0 -1 -1 -1 -1 -1 1 1 0 -1 8 6 -1 -1 -1 -1 -1 -1 3 5 9 4 1 9 -1 -1 -1 -1 -1 6 -1 -1 -1 -1 -1 -1 5 -1 -1 9 -1 -1 0 -1 -1 -1 -1 0 1 -1 3 -1 8 -1 1 -1 -1 -1 -1 2 5 6 2 6 -1 6 6 4 -1 9 -1 -1 -1 -1 5 8 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 5 -1 7 -1 -1 -1 -1 9 4 2 1 8 -1 -1 -1 3 4 -1 -1 -1 -1 -1 -1 -1 5 -1 -1 -1 -1 -1 4 -1 9 -1 -1 -1 3 -1 -1 3 -1 -1 7 4 1 -1 -1 -1 -1 -1 -1 -1 -1 7 8 -1 9 0 -1 -1 -1 2 6 -1 8 -1 -1 -1 -1 -1 2 -1 4 2 -1 -1 6 8 -1 -1 -1 -1 -1 4 -1 -1*/
 
//dfs postorder? left, right, root
/* ehh, źle zrozumiałem zadanie, nie chodzi o wszystkie ścieżki(suma wszystkich) modulo,
tylko o sume tych z danego poziomu modulo...
 OK XDD jednak myślałem poprawnie, ale modulo robiło mniew którymś miejscu w chuja
*/
//mozna tez uzyć bfs ze zmienną level i jakiejśc tablicy o ilości elementów level

void f(TreeNode*temp, int curVal, int &output){
    //po stworzeniu certyfikowanej zmiennej tempModulo już wszystko zadziałało
    int tempModulo = (((curVal*10)%1003) + temp->val)%1003;
    //MUSZE znalezc liścia i dopiero wtedy dodać
    if(temp->left==NULL && temp->right==NULL){
        //XDD, wyrażenie curVal*10 + temp-> val było i kompilator nie zwrócił błędu xdddd
        output += tempModulo;
        output = (output + 1003) % 1003; // dla bezpieczenstwa
        return;
    }
    if(temp->left !=NULL)
        f(temp->left, tempModulo, output);
    if(temp->right !=NULL)
        f(temp->right, tempModulo, output);
}


 
int Solution::sumNumbers(TreeNode* A) {
    
    int output = 0;
    
    f(A, 0, output);//1 = 10^0
    return (output + 1003) % 1003;
}