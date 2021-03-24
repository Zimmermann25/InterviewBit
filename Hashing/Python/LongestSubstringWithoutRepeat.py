class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        i = 0
        j = 0
        max = 0
        d = {}
        while i < len(A) and j < len(A):
            if d.get(str(A[j])) is None:  # jak jeszcze nie ma w slowniku to dodaj
                d[str(A[j])] = j  # indeks występienia
            else:  # jak juz jest w slowniku, to przesuwaj i az do napotkania
                d[str(A[j])] = j # ustaw index aktualnego wystąpienia powtórzonego chara
                # przesuwaj lewy wskaznik i usuwaj elementy ze slownika az do napotkania
                #znaku, który się powtórzył, 
                while str(A[i]) != str(A[j]):
                    del d[str(A[i])]
                    i += 1
                #w tym miejscu indeks poprzedniego i index aktualny danego znaku są takie same
                i+=1 #dlatego tutaj przejdz do następnego indeksu
            if (j - i + 1 > max):
                max = (j - i + 1)
    
            #print("i: ", i, "j: ", j, "d: ", d, "curMAX: ", max)
            j += 1
        #print(d)
        #print(sorted(d.items(), key=lambda x:x[0]))
        #print("dlugosc: ", len(d))
        return max