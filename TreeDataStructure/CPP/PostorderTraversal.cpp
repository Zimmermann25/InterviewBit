/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 

 
vector<int> Solution::postorderTraversal(TreeNode* A) {
    //postorder: left, right, root
    vector<int>output;
    stack<TreeNode *> s;
    s.push(A);
    TreeNode *curNode = A;
    //dwie flagi, pierwsza oznacza, czy lewy element wszedł na stos(wtedy prawy nie moze,
    //wypisanie też nie), druga sprawdza, czy moge wypisac curNode do output
    //w tej metodzie drzewo jest niszczone
    //ale w odpowiedziach też ciekawe rozwiązanie polegające na root, right, left
    //i odwróceniu wyniku na końcu
    
    //tutaj metoda polega mniej więcej na oznaczaniu i usuwaniu połączeń do dzieci,
    //które są właśnie wrzucane na stos, usunięcie połączenia oznacza, że dane dziecko
    //wleciało wcześniej na stos i można sprawdzić prawe, a jak oba są null, to wyposać
    bool rightFlag = true;
    bool bothFlag = true;
    while(s.size() >0 ){
        //left, right
        curNode = s.top();
        rightFlag = true;
        bothFlag = true;
        //spróbuj dodać lewy element
        if(curNode->left !=NULL){
            s.push(curNode->left);
            //oznacz ten node jako "zapamiętany", moge to zrobić, bo jego wskaznik
            //jest teraz zapamiętany na stosie
            curNode->left = NULL;
            rightFlag = false;
        }
        if(curNode->right != NULL && rightFlag){
            s.push(curNode->right);
            curNode->right = NULL;
            bothFlag = false;
        }
       
        if(rightFlag && bothFlag){//brak lewego i prawego potomka, mozna wpisać wartość
            //cout<<"in if"<<endl;
            output.push_back(curNode->val);
            s.pop();
        }
        
        
        
    }
    
    return output;
}