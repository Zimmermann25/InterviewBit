/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //ehh, trzeba użyć zmiennych globalnych, czyli problemy z kompilatorem nadciągają...
 //w tym zadaniu największą trudnością był kompilator i rozkmina jak zrobić bez globalnych
 //ale jednak użyłem globalnego stosu
stack<TreeNode*> myStack;

//od node temp dodawaj do stosu wartości po lewej(mniejsze od temp)
void leftChilds(TreeNode* temp){
    if(temp==NULL)return;
    else{
        while(temp !=NULL){
            myStack.push(temp);
            temp = temp->left;
        }
    }
    
}

BSTIterator::BSTIterator(TreeNode *root) {
    //czyszczenie sstosu tak na wszelki wypadek, bo w tym kompilatorze tak chyba trzeba
    while(!myStack.empty()){
        myStack.pop();
    }
    leftChilds(root);//wszystkie lewe dziecki na stos
}

/** @return whether we have a next smallest number */
bool BSTIterator::hasNext() {
    //w konstruktorze stos jest wypełniany rootem i lewymi wartościami, więc początkowo
    //nie będzie pusty, pusty będzie dopiero gdy nie będzie więcej elementów pozostałych
    if(myStack.empty()) return false;
    return true;
}

/** @return the next smallest number */
int BSTIterator::next() {
    if(!myStack.empty()){
        TreeNode *temp = myStack.top();
        myStack.pop();
        //usunąłem aktualny root, ale muszę dodać do stosu wartości z jego prawego poddrzewa
        //bo wartości z prawego poddrzewa tego node będą mniejsze niż wartość rodzica node
        leftChilds(temp->right);
        return temp->val;
    }
    
     
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */