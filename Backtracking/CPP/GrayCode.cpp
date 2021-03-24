vector<int> Solution::grayCode(int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
   
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    //samemu zrobiłem w pythonie metodą odbić lustrzanych z dodawaniem bitów
    //tutaj jest nie na podstawie bitów, ale na podstawie wartości
    //w komentarzu jest jeszcze fajne rozwiązanie z xorem
    vector<int> result;
    result.push_back(0); // początek
   
    for (int i = 0; i <A; i++) {
        int curSize = result.size();
        // push back all element in result in reverse order
        for (int j = curSize - 1; j >= 0; j--) {
            result.push_back(result[j] + (1 << i));
        } 
        //cout<<"curSize: "<<curSize<<endl;
        /*for(int k=0; k<result.size(); k++){
            cout<<result[k]<<" ";
        }
        
        cout<<endl;*/
    }
    
    
    return result;
    
}