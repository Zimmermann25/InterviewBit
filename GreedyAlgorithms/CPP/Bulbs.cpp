/* TLE, co mnie nie dziwi, choć myślałem, że tak trzeba w tym zadaniu
int counter = 0;
    int i = 0;
    while( i < A.size()){
        int temp = 0;
        int prevIndex = i;
        bool flag = true;
        //jak zarówka zapalona, to nic nie rob, przejdz w prawo
        if(A[i]==0){
            counter +=1; // włącz przełącznik
            //zmien stan wszystkich po prawej, ale tylko jeśli zmiana stanu aktualnej zarowki
            for(int j=i; j<A.size(); j++){
                if(A[j]==0){
                    A[j]=1;
                    if(flag){//zapamiętaj pozycję ostatniej jedynki w pierwszej ich serii
                        //przykład 1 1 1 1 0 0 1 0 1, to zapamiętaj indeks 3 i od tej pozyjcji
                        //dalej sprawdzaj
                        prevIndex = j;
                    }
                }
                else{
                    A[j] = 0;
                    flag = false;
                }
            }
        }
        i = prevIndex+1;
    }
*/

int Solution::bulbs(vector<int> &A) {
    
    //obserwacje, 2,4,6,8 itd wciśnięć przycisków nie zmienia finalnie stanu tych po prawej
    //na aktualnej pozycji sprawdzić także counter(ilość włączonych wcześniej)
    //mozna to było prościej zapisać, ale tutaj jest to możliwie łatwe w zrozumienuu
    int counter = 0;
    for(int i=0; i< A.size(); i++){
        if(A[i]==0){//jak jest 0 i parzysta ilość zmian stanu wcześniej, to trzeba przełączyć
            if(counter % 2==0)
                counter +=1;
        }
        //jak jest 1 i nieparzysta ilość zmian stanu wcześniej, to trzeba przełązyć tą pozycję
        else if(A[i]==1){
            if(counter % 2 == 1){ // zmieniony stan przez wcześniejsze switche
                counter +=1;
            }
        }
    }

    return counter;
}