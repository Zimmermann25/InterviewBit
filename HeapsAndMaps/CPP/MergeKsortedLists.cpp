/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/*10 1 34 7 37 54 75 82 92 94 98         9 14 22 34 36 37 55 56 64 91       8 17 28 30 37 47 56 58 68          6 3 5 47 56 76 96        6 6 18 35 43 63 95       6 9 22 34 55 56 73     1 57           3 23 28 85          8 5 31 35 38 56 69 73 79*/
/*10         9 8 20 38 44 55 65 66 79 87          2 68 72          5 5 55 61 73 89         2 30 73        4 28 73 84 96 3 54 82 83        5 15 33 38 94 100      1 4       5 22 32 42 64 86       2 11 78*/
 
/* generalnie w odpowiedziach wszyscy robili po prostu jeden duzy heap i dopiero potem tworzyli
nową listę, co było poprawne, choć zrobilem lepszym sposobem
Mój stos zawsze ma ilość elementów równą ilości łączonych list liniowych
dzięki czymu złożoność jest w większości przypadków mniejsza i wynosi NlogK,
zamiast NLOGN, zawsze K <=N, K oznacza ilość list, a N ilość wszytkich elementów
w pętli while zawsze 1 element wychodzi, ale kolejny wchodzi tylko jeśli aktualna
lista ma jeszcze elementy
*/
 
ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    //typ danych, który wchodzi do kolejki, typ w jakim dane będą składowane
    // i wg czego porownywac greater to minHeap
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>> > minHeap;
    for(int i=0; i<A.size(); i++){
        //czy jak będzie null na starcie, to się wysypie??
        //indeks 0 to aktualna minimalna wartosc i-tej listy liniowej(indeks 1)
        vector<int> temp = {A[i]->val, i}; // minimalna wartosc listy o indeksie i
        minHeap.push(temp);
    }
    
    //nowa lista liniowa
    ListNode *head = new ListNode(minHeap.top()[0]);//minimalna z pierwszych wartosci
    A[minHeap.top()[1]] = A[minHeap.top()[1]]->next;
    if(A[minHeap.top()[1]] != NULL){
        minHeap.push( {A[minHeap.top()[1]]->val, minHeap.top()[1] });
    }
    
    minHeap.pop(); // pop zawsze, powyzszy push niekoniecznie
    ListNode *temp = head;// kopia do wstawiania
    
    while(minHeap.size() >0){
        vector<int> curTop = minHeap.top(); 
        temp->next = A[ curTop[1] ];
        minHeap.pop(); // usun wartość dopiętą przed chwilą
        if( A[curTop[1]]->next !=NULL){
            A[curTop[1]] = A[curTop[1]]->next;
            //wchodzi {kolejna wartość i-tej listy i indeks aktualnej listy(zapisane w curTop)
            minHeap.push( { A[curTop[1]]->val, curTop[1] });
        }
        temp = temp->next;//na poczet kolejnych wywolan pętli while
    }
    
    return head;
}
