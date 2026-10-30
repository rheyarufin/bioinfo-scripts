segments=[]
count = {}
dna = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
for i in range(0,(len(dna)-2)):
    segments.append(dna[i:i+3])
for k_mer in segments:
    count.setdefault(k_mer,0)
    count[k_mer]=count[k_mer]+1
print(count)
def maxcount(counter):
    maxseq = ""
    maxcounter = max(counter.values())
    for k,v in counter.items():
        if(v==maxcounter):
            maxseq = maxseq + " " + k
    return maxseq
print(maxcount(count))