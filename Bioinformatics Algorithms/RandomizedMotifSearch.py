import random

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


def Profile(motifs):
    k = len(motifs[0])
    t = len(motifs) + 4   # Laplace
    
    profile = [[1]*k for _ in range(4)]
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
def RandomizedMotifSearch(Dna, k, t):
    
    # randomly select k-mers
    Motifs = []
    for dna in Dna:
       i = random.randint(0, len(dna) - k)
       Motifs.append(dna[i:i+k])
    BestMotifs = Motifs
    while True:
        ProfileMatrix = Profile(Motifs)
        # Motifs ← Motifs(Profile, Dna)
        Motifs = []
        for dna in Dna:
            Motifs.append(ProfileMostProbableKmer(dna, k, ProfileMatrix))
        
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs[:]
        else:
            return BestMotifs
            
dna="ATGAGGTC GCCCTAGA AAATAGAT TTGTGCTA"
dna_split=dna.split()
kk=3
tt=4
BestMotifs=None
BestScore=float('inf')
for i in range(1):
 result=RandomizedMotifSearch(dna_split,kk,tt)
 current_score=Score(result)
 if current_score<BestScore:
     BestScore=current_score
     BestMotifs=result
print(" ".join(BestMotifs))