#Bioinformatics problems
count = 0
dna = "ACTGTACGATGATGTGTGTCAAAG"
substring = "TGT"
for i in range(0,(len(dna)-len(substring))):
    if(dna[i:i+len(substring)]==substring):
      count = count+1
print(count)      