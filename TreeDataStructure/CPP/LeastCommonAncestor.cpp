/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//ten przykład dla 5 i 4 w treści zadania jest bezsensu, jak 5 może być swoim przodkiem...
//uważam, że odpowiedzią powinno być tam 3, chodzi o wspólnego przodka, a tam
//5 ma by swoim przodkiem, co jest bezsensu
//będą 2 wywołania w solution

/*
95 26 40 20 23 17 -1 -1 21 8 22 34 -1 -1 44 18 42 38 10 -1 -1 -1 37 -1 47 30 29 5 13 31 -1 -1 -1 -1 27 45 4 33 -1 -1 15 -1 -1 28 39 3 32 -1 -1 -1 -1 -1 25 6 -1 -1 46 9 -1 24 35 43 7 -1 -1 -1 -1 -1 41 16 11 14 -1 1 -1 -1 19 -1 12 -1 -1 -1 36 2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
11
38*/
//lowest oznacza, że pierwszy napotkany przodek, czy ten z najmniejszą wartością??
//super, myślałem i robiłem dla najmniejszej wartości przodka, nie dla pierwszego napotkanego
//a o to chodziło..., więc możliwe, że któreś ze wcześniejszych rozw było poprawne, ale
//psuł je  warunek w ostatniej pętli for

//zapamiętuje aktualną drogę, jeśli znajdzie cel, to droga jest przepisywana do paths
//na końcu szukam ostatniej wspólnej wartości, to jest odpowiedź
//było jeszcze jedno, liniowe rozwiązanie bez tablic, ale ono już bardziej skomplikowane
void f(TreeNode *root, vector<int> curPath,vector<vector<int>> &paths, int value, bool &found ){
    if(root==NULL)return;
    
    curPath.push_back(root->val);
    if(root->val == value){
        found = true;
        paths.push_back(curPath);
        return;
    }
    
    f(root->left, curPath, paths, value, found);
    f(root->right, curPath, paths, value, found);

}

int Solution::lca(TreeNode* A, int B, int C) {
    bool found1 = false;
    bool found2 = false;
    vector<int> path1;
    vector<int> path2;
    vector<vector<int>> paths;
    f(A, path1, paths, B, found1 );
    f(A, path2, paths, C, found2 );
    
    /*cout<<"size: "<<paths.size()<<endl;
    for(int i=0; i<paths[0].size(); i++){
        cout<<" "<<paths[0][i];
    }
    cout<<"bettween: "<<endl;
    for(int i=0; i<paths[1].size(); i++){
        cout<<" "<<paths[1][i];
    }*/
    
    if(found1==false || found2==false)return -1;
    int smallerLen = paths[0].size();
    if(paths[0].size() > paths[1].size())smallerLen = paths[1].size();
    
    int output = INT_MAX;
    for(int i=0; i< smallerLen; i++){
        if(paths[0][i]==paths[1][i]){
            output = paths[0][i]; // błedem było to: if(paths[0][i] < output)
        }
    }
    
    
    
    return output;
}