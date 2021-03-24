/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
//usunąć nody z jednym potomkiem, ale dzieci tego potomka zostają
//we wskazuwce jest sugerowane użycie postorder, ja zacząłem od preorder
//jest kilka dziwnych przypadków, ktore ciężko porówać do treści zadania
//w solutions w pythonie również ktoś podją taką próbę i zrobił, ja nie :(
//nie miałem zmiennej kierunku w funkcji f, przez co miałem za mało info
/*void f(TreeNode *child, TreeNode * parent){
    if(child==NULL) return;
    
    //jest tylko lewy potomek, przepięcie
    if(child->left!=NULL && child->right ==NULL){
        if(parent){
            parent->left = child->left;
            f(parent->left, parent);//rodzic bez zmian, ale potomek się zmienia(wnuk)
        }else{//przypadek specjalny dla root, gdzie parent=NULL
            parent = child;
            child = child->left;
            cout<<"first else"<<endl;
            // nie ma dalszego potomka w lewej gałęzi np.BFS 19, 3,NULL, usuń 3
            if(child==NULL)parent->left=NULL;
            else{
                cout<<"secondElse"<<" child: "<<child->val<< "left: "<<child->left->val<<endl;
                f(child->left, child);
                f(child->right, child);
            }
            
        }
    }
    
    //jest tylko prawy potomek, przepięcie
    else if(child->left==NULL && child->right !=NULL){
        if(parent){
            parent->right = child->right;
            f(parent->right, parent);//rodzic bez zmian, ale potomek się zmienia(wnuk)
        }
    }
    
    else{//oba potomki
        f(child->left, child);
        f(child->right, child);
    }
}*/
//na podstawie wskazówki i rozwiązania z pierwszego komentarza
//choć osobiście nie podoba mi się ta metoda postorder, wolałbym pre
//troche ciężko mi zrozumieć budowanie od dołu do góry, mam mylne wrażenie, żę wskazniki są
//gubione 
/*przykład dla bst 5 4 8 11 13 4 7 2 5 1
schodze możliwie dół(postorder),jak jest liść, to zwracam liść, f(7) = 7, potem badam f(2)
i zwracam 2, potem to 7 i 2 wchodzą do f(11), są 2 potomki, więc zwracam 11,
badam teraz prawe dziecko f(4), czyli null, teraz do f(4) wchodzi 11 i null, czyli trzeba 
usunąć node 4, a w miejsce f(4) wchodzi f(11), czyli 11 itd. 
                    5             
              f(4)          
        f(11)    f(N)  
    f(7)    f(2)
f(N) f(N)


                    5
              f(4)          
        f(11)    f(N)
    7    f(2)

*/
TreeNode *f(TreeNode *root){
    if(root==NULL)return NULL;
    root->left = f(root->left);
    root->right = f(root->right);
    
    //jest prawy potemek, ale brak lewego
    if( root->left==NULL && root->right!=NULL){
        return root->right;
    }
    else if( root->left!=NULL && root->right==NULL){
        //root->left wchodzi w miejsce root
        return root->left;
    }
    
    return root;//oba potomki są, albo liść i 2 nulle
}

TreeNode* Solution::solve(TreeNode* A) {
    /*if(A==NULL)return NULL;
    else if(A->left !=NULL && A->right==NULL)A = A->left;
    else if(A->left ==NULL && A->right!=NULL)A = A->right;
    
    f(A, NULL);
    return A;*/
    return f(A);
}