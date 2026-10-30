dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
kk=4
dd=1
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
seq="ATT"
dd=2
print(" ".join(Neighbours(seq,1)))
comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
def ReverseComplement(dna):
    reverse_dna = ""
    for base in reversed(dna):
        reverse_dna = reverse_dna + comp[base]
    return reverse_dna
def FrequentWordsWithMismatchesAndRC(text, k, d):
    freqMap = {}
    n = len(text)
    for i in range(0, n - k + 1):
        pattern = text[i:i+k]
        neighbourhood = Neighbours(pattern, d)
        for neighbor in neighbourhood:
            rc = ReverseComplement(neighbor)
            if neighbor not in freqMap:
                freqMap[neighbor] = 0
            freqMap[neighbor] += 1
            # also count reverse complement
            if rc not in freqMap:
                freqMap[rc] = 0
            freqMap[rc] += 1
    m = max(freqMap.values())
    patterns = []
    for p in freqMap:
        if freqMap[p] == m:
            patterns.append(p)
    return patterns
print(FrequentWordsWithMismatchesAndRC(dna,kk,dd))