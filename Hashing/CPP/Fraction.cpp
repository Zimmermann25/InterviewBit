string Solution::fractionToDecimal(int A, int B) {
	//identyczne w pythonie nie działa, problemy z zakresem intów i bitem znaku
	string fpart = "";
	string deci="";
	long long int  a = A,b = B;
	if( (a<0 && b>0) || (a>0 && b<0) )
		fpart+= "-";
 
	a = abs(a),b = abs(b);
	fpart += to_string(a/b);
	a = a%b;
	if(a == 0)return fpart;
	
	map<int,int> mp;
	while(a!=0 && mp.find(a) == mp.end())
	{
		mp[a] = deci.length();
		a = a*10;
		deci += to_string(a/b);
		a = a%b;
	}
	string recurr;
	
	if(a != 0)
	{
		string tt;
		recurr+=deci.substr(mp[a]);
		for(int i = 0;i<mp[a];i++)
		{
			tt+=deci[i];
		}
		recurr = '('+recurr+')';
		deci = tt+recurr;
		
	}
	
	return fpart+'.'+deci;
	//return "a";
}

