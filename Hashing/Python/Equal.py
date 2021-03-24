class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        # nie ma nawet opcji, żę mógłbym to zrobić w cpp xdxd
        # mozna to było zrobić o wiele łatwiej, w double for brać sume, dodać do dict
        # i w kazdym przebiegu sprawdzać, czy taka liczba jest już w dict
        
        output = []
        if len(A) < 4:return output
        d = {} # wszystkie
        C = 1
        D = 2
        for i in range(C,len(A)):
            tempDict = {}
            for j in range(i+1, len(A)):
                curSum = A[i] + A[j]
                if not d.get(curSum):
                    d[curSum] = [(i,j)]
                else:
                    d[curSum].append((i,j))
                    
        #print(d)
        # trzeba posortować dictionary wg values
        sorted_x = sorted(d.items(), key=lambda kv: kv[1])
        #print(sorted_x)
        import collections
        sorted_dict = collections.OrderedDict(sorted_x)
        #print(sorted_dict)
        Ai = 0
        Bi = 1
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                curSum = A[i] + A[j]
                if curSum in sorted_dict.keys():
                    CD = sorted_dict[curSum]
                    #print("len: ", len(CD))
                    for k in range(len(CD)):
                        if (i < CD[k][0]) and j != CD[k][0] and j !=CD[k][1]:
                            output = [i,j,CD[k][0], CD[k][1]]
                            return output
                        
        return output