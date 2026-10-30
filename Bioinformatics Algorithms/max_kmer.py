segments=[]
count = {}
max_count = 0
dna = "ACTGACTCCCACCCC"
for i in range(0,(len(dna)-2)):
    segments.append(dna[i:i+3])
for k_mer in segments:
    count.setdefault(k_mer,0)
    count[k_mer]=count[k_mer]+1
print(count)
def maxcount(counter):
    maxseq = 0
    for k,v in counter.items():
     if(v>maxseq):
        maxseq = v
        seq = k
    return seq
maxcount(count)