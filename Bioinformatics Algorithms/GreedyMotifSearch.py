def Score(motifs):
    k = len(motifs[0])
    score = 0
    for j in range(k):
        count = {}
        for motif in motifs:
            base = motif[j]
            count[base] = count.get(base, 0) + 1
        score += len(motifs) - max(count.values())
    return score
def NewHammingDistance(p,q):#Call stack
 count=0
 for i,j in zip(p,q):
    if(i!=j):
        count=count+1
 return count
def Profile(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile = [[0]*k for _ in range(4)]
    index = {'A':0,'C':1,'G':2,'T':3}
    for motif in motifs:
        for j in range(k):
            profile[index[motif[j]]][j] += 1
    for i in range(4):
        for j in range(k):
            profile[i][j] /= t
    return profile
def ProfileMostProbableKmer(text, k, profile):
    index = {'A':0,'C':1,'G':2,'T':3} 
    max_prob = -1
    best_kmer = text[0:k] 
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1      
        for j in range(k):
            prob *= profile[index[kmer[j]]][j]      
        if prob > max_prob:
            max_prob = prob
            best_kmer = kmer  
    return best_kmer
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = [dna[0:k] for dna in Dna]  
    first_string = Dna[0]  
    for i in range(len(first_string) - k + 1):
        Motifs = []
        Motifs.append(first_string[i:i+k])      
        for j in range(1, t):
            profile = Profile(Motifs)
            next_kmer = ProfileMostProbableKmer(Dna[j], k, profile)
            Motifs.append(next_kmer)      
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs   
    return BestMotifs
data="GGCGTTCAGGCA AAGAATCAGTCA CAAGGAGTTCGC CACGTCAATCAC CAATAATATTCG"
dna_list=data.split()
kk=3
tt=5
result=GreedyMotifSearch(dna_list,kk,tt)
print(" ".join(result))