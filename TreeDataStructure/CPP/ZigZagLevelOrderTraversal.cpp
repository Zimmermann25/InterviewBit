/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//moge zrobić zwykłe BFS i odwrócić co drugi wiersz xd, ale może spróbuje inaczej
//potrzebuje dodawać nulle jako separatory pozycji i zmienną direction
void f(TreeNode *root, vector<vector<int>> &output, queue<TreeNode* > q){
    if(root==NULL)return;
    TreeNode *temp = root;
    bool direction = 0; //1 od lewej do prawej, 0 od prawej do lewej
    vector<int>tempArr;
    while(q.size() > 0 || temp){
        //cout<<"curSize: "<<q.size()<<endl;
        temp = q.front();
        
        //if(temp)cout<<"before: "<<temp->val<<endl;
            
        q.pop();
        /*cout<<"pop before iff"<<endl;
        if(q.size() > 0){
            cout<<"inner iff ";
            TreeNode *temp2= q.front();
            if(temp2)cout<<"after: "<<temp2->val<<endl;
        }*/
        
        
        if(temp==NULL){//null oznacza koniec poziomu
            //q.pop();//musze je usunąć jak je znajde, bo zaraz dodaje NULL dla kolejnego poziomu
            //direction = ~direction;
            output.push_back(tempArr);
            //cout<<"found null, insert"<<endl;
            tempArr.clear();
            if(q.size() >0)
                q.push(NULL); //oznaczenie końca następnego poziomu(dla wartośći obecnych w kolejce)
        }
        else{
            //cout<<"else"<<endl;
            tempArr.push_back(temp->val);
            //if(direction){//jak od lewej do prawej, to najpierw lewe do kolejki
                if(temp->right)q.push(temp->right);
                if(temp->left)q.push(temp->left);
                
            /*}else{
                if(temp->right)q.push(temp->right);
                if(temp->left)q.push(temp->left);
            }*/
        }
        
    }
    
    
    
}

vector<vector<int> > Solution::zigzagLevelOrder(TreeNode* A) {
    vector<vector<int>> output;
    queue<TreeNode* > q;
    q.push(A);

    q.push(NULL);//pierwszy separator
    f(A, output, q);
    
    //zamień co drugi wiersz, bez roota, a pierwszy wiersz też normalnie
    for(int i=2; i<output.size(); i++){
        if(i % 2==0){
            for(int j=0; j<output[i].size()/2; j++){
                swap(output[i][j], output[i][ output[i].size()-j-1 ]);
            }
        }
    }
    
    //cout<<"size: "<<q.size();
    return output;
}
