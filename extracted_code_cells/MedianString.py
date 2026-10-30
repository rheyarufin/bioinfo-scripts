def NewHammingDistance(p,q):#Call stack
 count=0
 for i,j in zip(p,q):
    if(i!=j):
        count=count+1
 return count
def DistanceBetweenPatternandStrings(pattern,dna):
   k=len(pattern)
   distance=0
   for stringtext in dna:
      HammingDistance=float('inf')
      for i in range(0,(len(stringtext)-k+1)):
         k_mer=stringtext[i:i+k]
         d=NewHammingDistance(k_mer,pattern)
         if HammingDistance>d:
            HammingDistance=d
      distance=distance+HammingDistance
   return distance
kk=7
string="CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"
dna_list=string.split()
def MedianString(dna,k):
   distance=float("inf")
   for Pattern in dna:
      for i in range(0,(len(Pattern)-k+1)):
         k_mer=Pattern[i:i+k]
         med=DistanceBetweenPatternandStrings(k_mer,dna)
         if distance>med:
            distance=med
            Median=k_mer
   return Median
result=MedianString(dna_list,kk)
print(result)
