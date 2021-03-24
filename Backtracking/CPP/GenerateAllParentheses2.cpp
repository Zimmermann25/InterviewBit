void f(int A, int left,int right, string tempStr, vector<string> &output){
    // więcej zamknietych przed otwartymi, albo przekroczenie ilości nawiasów
    /*przykład branch and bound, teoretycznie wysokosc drzewa wywołań to 2*A
    jednak w momencie występienia błędnej sytuacji(więcej prawych niz lewych, przekroczenie
    limitu A nawiasów), to ta gałąź jest zabijana i nie są kontynuowane wywołania z niej,
    więc w rzeczywistości nie będzie 2^(2*A) wywołań
    */
    if(right> left || left>A || right > A)return; 
    
    //przypadek, ze wszystko jest ok i można dołączyć
    if(left + right == 2*A){
        output.push_back(tempStr);
    }
    
    f(A, left+1, right, tempStr+"(", output);//dopisz otwarty nawias

    f(A, left, right+1, tempStr+")", output);//dopisz zamknięty nawias
}



vector<string> Solution::generateParenthesis(int A) {
    
    vector<string> output;
    //od razu daje otwarty, bo nie moze się zaczynać zamknietym
    f(A, 1, 0, "(", output);
    
    return output;
}