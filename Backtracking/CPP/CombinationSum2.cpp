#include <algorithm>

void f(vector<int> &A, int curIndex, int curSum, int targetSum, vector<int> temp, vector<vector<int>> &output){
    
    if (targetSum == curSum){// jak znajdzie sume, to dodaje do output
        output.push_back(temp);
        return;
    }
    else{
        int i = curIndex;//pozycja początkowa do następnego wywołania
        while(i < A.size()){
            //cout<<"i: "<<i<<" curIndex: "<<curIndex<<" curSum: "<<curSum<<endl;
            //i > curIndex, bo pierwsze wystąpienie od zadanego miejsca się nie liczy
            //czyli pierwsze wywołanie ZAWSZE jest ok, ale potem tak długo jak jest ta
            //sama liczba to kolejne wywołanie jest omijane
            //czyli dla 1,2,2,2,3 lewe gałęzie drzewa zawsze będą, ale prawe będą obcięte
            //ze wzgledu na ten warunek
            if (i >curIndex && A[i] == A[i-1]){
                i++; // bez tego był potężny błąd xddd
                continue;
            }
            else if(curSum + A[i] <= targetSum){
                temp.push_back(A[i]);//dodaj aktualną liczbę do tablicy temp
                //idź dalej z tą liczbą
                f(A, i+1, curSum+A[i], targetSum , temp, output);
                temp.pop_back();//i jak już dojdzie do końca z tą liczbą, to ją usun
            }
            else {//jek przekroczy sume, to nie sprawdzaj dalej
                return;
            }
            i++;
        }
    }
    return;
}


vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    
    vector<vector<int>> output;
    vector<int> temp;
    sort(A.begin(), A.end());
    f(A, 0, 0, B, temp, output);
    
    return output;
}