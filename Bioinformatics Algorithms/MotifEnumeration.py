def NewHammingDistance(p,q):#Call stack
 count=0
 for i,j in zip(p,q):
    if(i!=j):
        count=count+1
 return count
def Neighbours(pattern, d):
    if d==0:
        return [pattern]
    if len(pattern)==1:
        return['A','C','G','T']
    neighbourhood=[]
    suffix_neighbours=Neighbours(pattern[1:],d)
    for text in suffix_neighbours:
        if NewHammingDistance(pattern[1:],text)<d:
            for x in ['A','C','G','T']:
                neighbourhood.append(x+text)
        else:
            neighbourhood.append(pattern[0]+text)
    return neighbourhood
def MotifEnumeration(dna,k,d):
    pattern=set()
    for k_mer_Patterns in dna:
        for i in range(0,(len(k_mer_Patterns)-k+1)):
         patterns=k_mer_Patterns[i:i+k]
         neighbourhood=Neighbours(patterns,d)
         for j in range(0,len(neighbourhood)):
          neighbours=neighbourhood[j]
          found=True
          for seq_string in dna:
             match=False
             for z in range (0,len(seq_string)-k+1):
              seq=seq_string[z:z+k]
              if NewHammingDistance(seq,neighbours)<=d:
               match = True
               break
             if not match:
              found=False
              break
          if found:
            pattern.add(neighbours)
    return pattern
text=["GGGACGTTACGGAACAGTCCTGTAC","TAATTCGGACCCGGTATGCCGGAGA", "AATCATGGACACCCAAAGGGGTCGC", "TGGACACTTGGGCGTTAGGATCCAG", "AGGTGGATAAGTTACTAAGCGGGAC","GGTAGGTTTCTAGTATTCGGAGGAC"]
kk=5
dd=1
result=MotifEnumeration(text,kk,dd)
print(" ".join(result))
       