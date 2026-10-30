def NewHammingDistance(p,q):
 count=0
 for i,j in zip(p,q):
    if(i!=j):
        count=count+1
 return count
count = 0
dna = "CCTGAAAGAAATAGATACCCTGAAAATACTAGGAAAGAAAATACCCTGAAATAGCCTTAGCCTTAGATACATACTAGCCTTAGGAAAATACATACCCTCCTATACATACCCTCCTGAAAATACCCTATACGAAATAGATACCCTCCTCCTCCTCCTGAAACCTATACTAGCCTGAAATAGATACATACATACTAGCCTCCTATACATACATACCCTTAGGAAACCTATACGAAACCTTAGTAGTAGCCTCCTCCTCCTGAAATAGTAGCCTCCTATACCCTGAAAGAAAATACGAAAATACCCTGAAAGAAAGAAACCTGAAAGAAAATACATACATACTAGTAGCCTGAAAGAAACCTTAGCCTCCTCCT"
k=6
ls={}
sequences=[]
total_seq=[]
freq={}
d=3
for i in range(0,(len(dna)-k+1)):
    seq=dna[i:i+k]
    ls.setdefault(seq,0)
    ls[seq]=ls[seq]+1
max_ls=max(ls.values())
for seq,n in ls.items():
     if(n==max_ls):
          sequences.append(seq)
print(sequences)
for s in sequences:
     for seq in ls.keys():
       if(s!=seq):
          count=NewHammingDistance(s,seq)
          if(count<=d):
           total_seq.append(seq)
       elif(s==seq):
           total_seq.append(seq)
print(f"All matching patterns/neighbours within",d," mismatches: ")
print(" ".join(total_seq))

