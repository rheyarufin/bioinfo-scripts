dna = "TGGTATGGGTGGTAGGGGCTTGGTGTGGTACTACTACTATGTGGGGTAGTACTTCTATGGTATGTGCTTTGTGCTTCTTGTAGTAGTATGCTTCTTCTACTAGTATGGTAGTAGTAGTATGCTACTTGTAGTAGGCTTGTACTTCTTCTACTAGTACTAGGCTAGGGTACTACTTGGTGGTACTTCTTCTTCTTCTTTGTGGTACTTTGCTATGGGCTAGGGGGTAGGTGGGCTACTA"
comp = {'A':'T','T':'A','G':'C','C':'G'}
k=7
d=2
def ReverseComplement(dna):
    reverse_dna=""
    for base in reversed(dna):
       reverse_dna=reverse_dna+comp[base]
    return reverse_dna
def NewHammingDistance(p,q):
 count=0
 for i,j in zip(p,q):
    if(i!=j):
        count=count+1
 return count
def Neighbours(pattern, d):
    if d==0:
        return pattern
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
def FrequentWordsWithMismatches(text,kk,dd):
    patterns=[]
    freqMap={}
    n=len(text)
    for i in range(0,n-kk+1):
        pattern=text[i:i+kk]
        neighbourhood=Neighbours(pattern,dd)
        for j in range(0,len(neighbourhood)):
            neighbour=neighbourhood[j]
            rc=ReverseComplement(neighbour)
            if neighbour not in freqMap:
                freqMap[neighbour]=1
            else:
                freqMap[neighbour]=freqMap[neighbour]+1
            if rc not in freqMap:
                freqMap[rc]=1
            else:
                freqMap[rc]=freqMap[rc]+1      
    m=max(freqMap.values())
    for pattern in freqMap:
        if freqMap[pattern]==m:
            patterns.append(pattern)
    patterns=" ".join(patterns)
    return patterns
result=FrequentWordsWithMismatches(dna,k,d)
print(result)

