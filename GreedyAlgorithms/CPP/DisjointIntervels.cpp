 
//w edytorze interviewbit czasami tle, czasami correct
bool compare(const vector<int> A, const vector<int> B ){
	if(A[0]==B[0])return A[1] < B[1];
	return A[0] < B[0];
}
 
int Solution::solve(vector<vector<int> > &A) {
	sort(A.begin(), A.end(), compare);
	int prevBegin = A[0][0];
	int prevEnd = A[0][1];
	int counter = A.size(); //domyślnie wszystkie są ok
	/*for(int i=0; i<A.size(); i++){
		for(int j=0; j<2; j++){
			cout<<A[i][j]<<" ";
		}
		cout<<endl;
	}*/
	
	for(int i=0; i<A.size()-1; i++){
		//cout<<"i: "<<i<<"A[i][0]: "<<A[i][0]<<"prevEnd: "<<prevEnd<<" counter: "<<counter<<endl;
		if(A[i+1][0] <= prevEnd ){//jest overlap, jeden z nich pomin
			//wybierz, który może zostać, na podstawie końca ich czasu
			if(prevEnd > A[i+1][1]){
				prevEnd = A[i+1][1];
			}
			counter -=1;
			
		}else{//nie ma overlap, prevEnd = koniec nowego przedziału
			prevEnd = A[i+1][1];
		}
 
		
	}
	
	
	return counter;
}

